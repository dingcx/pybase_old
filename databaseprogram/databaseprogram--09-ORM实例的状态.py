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

#2019-08-03 14:15:15,463 INFO sqlalchemy.engine.base.Engine {'param_1': 2}如果找不到的话
# student = session.query(Student).get(2)
student = session.query(Student).get(6)
print(student)

from sqlalchemy.orm.state import InstanceState

state = sqlalchemy.inspect(student)

print(state.persistent)
print(state.pending)
print(state.transient)

print('---------------')

s1 = Student(id=1,name="dingcx",age=27)
state = sqlalchemy.inspect(s1)

print(state.persistent)
print(state.pending)
print(state.transient)


def getstate(i,instance):
    from sqlalchemy.orm.state import InstanceState
    state = sqlalchemy.inspect(instance)
    state = "{},session_id={},attached={},transient={},pending={},persistent={},deleted={},detached={}".format(i,state.session_id,state._attached,state.transient,state.pending,state.persistent,state.deleted,state.detached)
    print(state)
    print('-' * 30,end='\n\n')



getstate(1,s1)
session.add(s1)
getstate(2,s1)
session.commit()
getstate(3,s1)


student = session.query(Student).get(1)
getstate(4,student)

session.delete(student)
getstate(5,student)
session.flush()
getstate(6,student)


session.commit()
getstate(7,student)

student = Student(name="ding",age=28)#transient=True此时的状态是，实体未加入session中
getstate(8,student)

session.add(student)
getstate(9,student)

session.flush()
getstate(10,student)

session.commit()
getstate(11,student)