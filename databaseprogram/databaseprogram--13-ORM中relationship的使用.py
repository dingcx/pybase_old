#!/bin/env python
# -*- coding: utf-8 -*-


import sqlalchemy
from sqlalchemy import create_engine,Column,Integer,String,Date,Enum,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship
import enum


class GenderEnum(enum.Enum):
    M = 'M'
    F = 'F'


USER = 'root'
PWD = 'root'
HOST = 'localhost'
DB = 'test'

engine = create_engine('mysql+pymysql://{}:{}@{}/{}'.format(USER,PWD,HOST,DB),echo=True)


Base = declarative_base()


class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(64),nullable=False)
    age = Column(Integer)

    def __repr__(self):
        return "<Student {} {} {}>".format(self.id,self.name,self.age)


Session = sessionmaker(bind=engine)
session = Session()


class Employee(Base):
    __tablename__ = 'employees'

    emp_no = Column('emp_no',Integer,primary_key=True)
    birth_date = Column(Date,nullable=False)
    first_name = Column(String(14),nullable=False)
    last_name = Column(String(16),nullable=False)
    gender = Column(Enum(GenderEnum),nullable=True)
    hire_date = Column(Date,nullable=False)

    #从员工的角度，看这个员工属于哪个部门
    departments = relationship('Dept_emp')#这也是一个list

    def __repr__(self):
        return "<Emploee no={} name='{} {}' gender={} departments={}>".format(self.emp_no,self.first_name,self.last_name,self.gender.value,self.departments)


def showresults(emps):
    for x in emps:
        print(x)


class Department(Base):
    __tablename__ = 'departments'

    dept_no = Column(String(4),primary_key=True)
    dept_name = Column(String(40),nullable=False,unique=True)

    def __repr__(self):
        return "<Dept no={} name={}>".format(self.dept_no,self.dept_name)


#多对多的关系表
class Dept_emp(Base):
    __tablename__ = 'dept_emp'

    #涉及到外键的时候，必须在类型后面加上ForeignKey('必须是表名.表所对应的字段')
    emp_no = Column(Integer,ForeignKey('employees.emp_no'),primary_key=True)
    dept_no = Column(String(4),ForeignKey('departments.dept_no'),primary_key=True)
    from_date = Column(Date,nullable=False)
    to_date = Column(Date,nullable=False)

    def __repr__(self):
        return "<Dept_emp eno={} dno={}>".format(self.emp_no,self.dept_no)


print('relationship的使用')
emp = session.query(Employee).join(Dept_emp,Employee.emp_no == Dept_emp.emp_no).filter(Employee.emp_no == 10009)
print(emp.all())#[<Emploee no=10009 name='Sumant Peac' gender=F departments=[<Dept_emp eno=10009 dno=d006>]>]


