Following Packages are needed 
```
pip install mysql-connector-python 
pip install configparser 
pip install ttkthemes
```
Configure the DB detals in db_config.cfg file
```
[MYSQL]
host = localhost
database = atp
user = admin
password = <>
```
Run the db_scripts.sql in MySQL to create database, tables and populate master data 
```
mysql> source db_scripts.sql
```
