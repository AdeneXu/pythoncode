"""
  生成随机的数据表信息
"""
import pymysql
from faker import Faker

conn = pymysql.connect(host='localhost',port=3306,user='root',password='abcd.1234',db='faker',charset='utf-8')

cursor = conn.cursor()

sql = """
create table user(
    id int RRIMARY KEY auto_increment,
    username VARCHAR(20),
    password VARCHAR(20),
    address VARCHAR(35)
)
"""
cursor.execute(sql)

fake = Faker('zh_CN')
for i in range(20):
    sql = """insert into user(username,password,address)
             values('%s','%s','%s')"""\
            %(fake.user_name(),fake.password(special_chars=False),fake,address())
    cursor.execute(sql)

conn.commit()
cursor.close()
conn.close()

