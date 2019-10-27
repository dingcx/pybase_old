#!/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''
__author__ = 'dcx'
__mtime__ = '2019/7/25'
# code is far away from bugs with the god
'''
import sqlalchemy
from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



USER = 'root'
PWD = 'root'
HOST = 'localhost'
DB = 'sakila'


print(sqlalchemy.__version__)

'''
创建连接,echo=True引擎是否打印执行的语句，调试的时候打开很方便
创建引擎不会马上连接数据库，直到让数据库执行任务时才连接
'''
engine = create_engine('mysql+pymysql://{}:{}@{}/{}'.format(USER,PWD,HOST,DB),echo=True)

#声明映射，SQLAlchemy大量使用元编程
Base = declarative_base()

#Mapper
class Student(Base):#一定要继承Base
    __tablename__ = 'student' #必须制定表名
    id = Column(Integer,primary_key=True,autoincrement=True)#字段定义，类属性
    name = Column(String(64),nullable=False)
    age = Column(Integer)

    def __repr__(self):
        return "<Student {} {} {}>".format(self.id,self.name,self.age)

# print(repr(Student.__table__))
# s = Student(name='tome');
# print(s)
# s.age = 30
# print(s)
#
# #创建表
# #Base.metadata.create_all(bind=engine)
#
# #构建Session类,session对象线程不安全，所以不同线程应该使用不同的session对象
Session = sessionmaker(bind=engine)
# #session实例
session = Session()
#
# #这种方式不是很合适
# #session.add(s)
# #session.commit()
# #session.rollback()
#
# try:
#     #s.age = 50
#     session.add_all([s])
#     session.commit
# except Exception as e:
#     print(e)
#     session.rollback()

students = session.query(Student)#students = session.query(Student).get(2)这样的会就会立即加载
print(students)#到这里，即便是打印students，也不会被认为是使用了查询出来的数据，只是会拼接查询语句
#z这种现象就是懒加载了
#print(list(students))#到这里了，才会认为开始使用了数据，所以开始加载
for x in students:
    print(x)


for x in students:
    print(x)



