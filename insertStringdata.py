#coding:utf-8
import pymysql

db = pymysql.connect("192.168.3.233","root","new@test","daclogin")

#使用cursor()方法获取操作游标
cur = conn.cursor()


