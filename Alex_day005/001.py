import MySQLdb


conn = MySQLdb.connect(host='192.168.1.31',
user='root', passwd='123456', port=3306)
cur = conn.cursor()
cur.execute('create database if not exists s6py')
conn.select_db('s6py')
cur.execute("""
    create table stu_info(
    id int(10) not null primary key auto_increment,
    name char(10) not null,
    phone int(12) not null,
    class char(20)
    );
"""
)

info = ['Hanxin',1850023903,'Python S6']

cur.execute("""
    insert into stu_info values %s
""" % info)
cur.commit()
cur.close()
conn.close()
