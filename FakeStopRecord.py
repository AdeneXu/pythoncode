
"""
PyMySQL 封装了MYSQL驱动的python驱动，一个能使python连接到Mysql的库
python version >= 3.4
"""

import pymysql
import datetime,time
import random

#连接DB
conn = pymysql.connect(host="192.168.3.222",user="root",password="abcd.1234",database="work",charset="utf8")

#得到一个可以执行sql语句的光标对象
cursor = conn.cursor()

for n in range(5):
    ran1 = random.randint(5,20)

    print("============ran = %d", ran1)

    cur_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    stop_time = datetime.datetime.now() - datetime.timedelta(minutes=ran1)
    start_time = stop_time + datetime.timedelta(minutes=ran1)

    sql = "INSERT into i_plc_machinefaultsummary(machID,createTime,starttime,stoptime) VALUES(%s,%s,%s,%s)"
    data = [68,cur_time,start_time.strftime('%Y-%m-%d %H:%M:%S'),stop_time.strftime('%Y-%m-%d %H:%M:%S')]

    cursor.execute(sql,data)
    conn.commit()

    time.sleep(120)

cursor.close()
conn.close()