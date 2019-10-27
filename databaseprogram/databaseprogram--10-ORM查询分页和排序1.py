#!/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''
__author__ = 'dcx'
__mtime__ = '2019/7/25'
# code is far away from bugs with the god
所以条件选择有三种方式：
    and_(),or_(),not_(),in_()
    &,|,~
    filter()
'''
import sqlalchemy
from sqlalchemy import create_engine,Column,Integer,String,Date,Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import enum


#Python中的枚举
class GenderEnum(enum.Enum):
    M = 'M'
    F = 'F'


USER = 'root'
PWD = 'root'
HOST = 'localhost'
DB = 'test'

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


# #构建Session类,session对象线程不安全，所以不同线程应该使用不同的session对象
Session = sessionmaker(bind=engine)
# #session实例
session = Session()


class Employee(Base):
    __tablename__ = 'employees'

    emp_no = Column('emp_no',Integer,primary_key=True)
    birth_date = Column(Date,nullable=False)
    first_name = Column(String(14),nullable=False)
    last_name = Column(String(16),nullable=False)
    gender = Column(Enum(GenderEnum),nullable=True)
    hire_date = Column(Date,nullable=False)

    def __repr__(self):
        return "<Emploee no={} name='{} {}' gender={}>".format(self.emp_no,self.first_name,self.last_name,self.gender.value)


def showresults(emps):
    for x in emps:
        print(x)


#查询id大于10018的employee !=  == <=
emps = session.query(Employee).filter(Employee.emp_no >= 10018)
#emps = session.query(Employee).filter(Employee.emp_no == 10018)
showresults(emps)

print('-' * 30)
emps = session.query(Employee).filter(Employee.emp_no >= 10018).filter(Employee.gender == 'F')
showresults(emps)

#支持数据库的与或非
from sqlalchemy import and_,or_,not_

print('-' * 30)
emps = session.query(Employee).filter(and_(Employee.emp_no >= 10018,Employee.gender == 'F'))
showresults(emps)

print('使用Python的与或非，要加上括号，避免优先级的问题')
emps = session.query(Employee).filter((Employee.emp_no >=10018) & (Employee.gender == 'F'))
showresults(emps)

print('in和not in 的使用')
emps = session.query(Employee).filter(Employee.emp_no.in_([10001,10002]))
showresults(emps)

emps = session.query(Employee).filter(~Employee.emp_no.in_([10001,10002]))
showresults(emps)

print('-' * 30)
emps = session.query(Employee).filter(Employee.emp_no.notin_([10001,10002]))
showresults(emps)



print('like的使用')
emps = session.query(Employee).filter(Employee.first_name.like('P%'))
showresults(emps)

print('-' * 30)
emps = session.query(Employee).filter(~Employee.first_name.like('P%'))
showresults(emps)
print('-' * 30,'ilike忽略大小写')
emps = session.query(Employee).filter(Employee.first_name.notlike('P%'))
showresults(emps)

print('-' * 30)
emps = session.query(Employee).filter(Employee.emp_no > 10015).order_by(Employee.first_name)
showresults(emps)

print('降序')
emps = session.query(Employee).filter(Employee.emp_no > 10015).order_by(Employee.first_name.desc())
showresults(emps)


print('分页')
emps = session.query(Employee).limit(5)
showresults(emps)
print('按照这样的方式就可以继续分页')
emps = session.query(Employee).limit(5).offset(5)
print(emps)
#以下的就是消费者方法,消费者方法没执行一次，都会查询一次数据库
#print(list(emps))
#print(emps.all())#返回的是list
#print(emps.one())#返回一个Employee对象，而且查询的结果必须是一个，否则就异常了
print('返回结果集中的一个，一下调用两次是为了说明first方法没有游标的概念')
print(emps.first())#查无数据的时候，返回None
print('-' * 30)
print(emps.first())

from sqlalchemy import func
print('演示scalar函数的使用')
emp = session.query(Employee).filter(Employee.emp_no == 10018)
print(emp.scalar())

print('聚合函数')
emps = session.query(func.count(Employee.emp_no),func.max(Employee.emp_no),func.min(Employee.emp_no),func.avg(Employee.emp_no),func.sum(Employee.emp_no))
print(emps)
print(emps.one())
print(emps.scalar())


print("分组")
emps = session.query(Employee.gender,func.count(Employee.emp_no),func.max(Employee.emp_no),func.min(Employee.emp_no),func.avg(Employee.emp_no),func.sum(Employee.emp_no)).group_by(Employee.gender)
print(emps)
print(emps.all())




