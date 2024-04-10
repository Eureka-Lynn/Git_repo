import mysql.connector

conn=mysql.connector.connect(user='root',password='200549',database='test')
cursor=conn.cursor()

cursor.execute('create table user (id varchar(20) primarykey,name varchaar(20))')

cursor.execute('insert into user (id,name)values(%s,%s)',['1','Micheal'])

print(cursor.rowcount)