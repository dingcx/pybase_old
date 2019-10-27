#!/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''
__author__ = 'dcx'
__mtime__ = '2019/7/25'
# code is far away from bugs with the god
Python中：
    所有非object类都继承自object类
    所有类的类型包括type类都是type
    type类继承自object类，object类的类型也是type类
'''
#这个和后面的Column非常相似
class Field:
    def __init__(self,name=None,*,pk=False,nullable=False):
        self.name = name
        self.pk = pk
        self.nullable = nullable

    def __repr__(self):
        return '<Field {}>'.format(self.name)


class ModelMeta(type):
    def __new__(cls, name,bases,attrs ):
        print(cls)
        print(name)
        print(bases)
        print(attrs)
        tblname = '__tablename__'

        #使用元类动态注入表名
        if tblname not in attrs.keys():
            attrs[tblname] = name

        pks = []

        for k,v in attrs.items():
            if isinstance(v,Field):
                print(k)
                print(v)
                #print(v.name)
                if v.name is None:
                    v.name = k
                if v.pk:
                    pks.append(v)
        attrs['__primarykeys__'] = pks

        return super().__new__(cls,name,bases,attrs)


class MetaBase(metaclass=ModelMeta):
    pass


class User(MetaBase):
    id = Field(pk=True,nullable=False)
    name = Field('username',nullable=False)
    age = Field()


print('+' * 40)
print(User.__dict__)





