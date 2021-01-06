#!/usr/bin/python3

import pymysql

db = pymysql.connect("192.168.50.191","root","test123", local_infile = 1)
cursor = db.cursor()


create = """CREATE DATABASE IF NOT EXISTS logging"""

cursor.execute(create)

db.close()

db = pymysql.connect("192.168.50.191","root","test123","logging", local_infile = 1)

cursor = db.cursor()

sql = """CREATE TABLE IF NOT EXISTS tablelogs (
   DATE DATE,
   TIME TIME,
   HOST VARCHAR(20),
   USER VARCHAR(15),
   IP VARCHAR(20) )"""


cursor.execute(sql)


sqlpass = """load data local infile "/mnt/data/out/outputlogs" into table tablelogs FIELDS TERMINATED BY ' ' LINES TERMINATED BY '\n';"""

cursor.execute(sqlpass)


clear = """DELETE FROM tablelogs WHERE date < DATE_SUB(NOW(), INTERVAL 30 day);"""

cursor.execute(clear)

db.commit()
db.close()

