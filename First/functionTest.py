#!/bin/env python
#
#主要写函数测试的代码


def fn(x):
    for i in range(x):
        if i > 3:
            return i
        else:
            print("{} is not greater than 3".format(x))


print(fn(3))
print(fn(6))


def showlist():
    return [1,3,5]


def showlist2():
    #返回的是一个元组
    return 1,3,5


print( showlist() )
print(type(showlist2()))

x,y,z = showlist2()
#可以使用解构来提取
print(x,y,z)


'''
函数的嵌套
    内嵌函数的作用域是当前函数内部
'''
def outer():
    def inner():
        print("inner")
    print("outer")
    inner()


outer()

'''
out_var = 1

#外部的变量也不能在内部使用
def show():
    out_var += 1
    print(out_var)

show()
'''

var = 1


def show():
    '''
    #所以外部变量对于函数来说只是可读不可写？
    var += 1
    '''
    print(var)


show()


def outer1():
    o = 65

    def inner():
        print("inner {}".format(o))
        print(chr(o))

    print("outer {}".format(o))
    inner()


outer1()


var = 3


def foo():
    y = var + 1
    '''
    如果这里加上一个变量声明，那么久表示var是一个内部变量，未声明就使用时不可以的
    var = 1
    
    '''
    return y


print("----------------")
print(foo())


var = 4


def foo2():
    print(var)


foo2()


'''
global
'''
var = 10
print("var id is {}".format(id(var)))


def foo4():

    global var2#如果外部没有声明变量呢？
    global var
    var += 1
    print(var)
    print("id var is {}".format(id(var)))
    var2 = 19


foo4()
print(var)#外面的var的值也改变了
print(var2)
z = 200


def foo12():
    z = 100

    def bar():
        global z
        z = z + 1
    print(1,z)

    bar()
foo12()
print(2,z)


'''
为了理解闭包

'''
def counter():
    c = [0]
    def inc():
        c[0] += 1
        return c[0]
    return inc #这是一个复杂类型，地址，引用


test = counter()#返回 函数inc  foo=>incs
print(test(),test())
c = 100
print(test())

print("nonlocal的使用-----------------")


'''
nonlocal的使用
'''


def counter2():
    m = 9

    def inc():
        nonlocal m
        m += 1
        return m

    return inc


test2 = counter2()
print(test2(),test2())
#print(type(m))
c = 100
print(test2())


print("形参的默认值-----------------")
'''
默认值得作用域
    函数的默认值就是放置在该函数对象的__defaults__属性中
    函数的key-word only对放置在__kwdefaults__中
    
'''
def test4(xyz=[1]):
    xyz.append(1)
    print(xyz)
print("刚刚定义的时候函数的缺省值{}".format(test4.__defaults__))
'''
输出：
[1, 1]
[1, 1, 1]：所以如果传参的时候使用了默认值的情况，而且默认值是一个可变类型，那么就一定要注意了。
'''
test4()
test4()
#print(xyz)
test4([1])
test4([1])

def test5(xyz):
    xyz.append(1)
    print(xyz)

'''
输出：
[1, 1]
[1, 1, 1]
test5()
test5()
如果函数定义没有默认值的话，函数调用的时候就不能使用默认值
'''

#print(xyz)
test5([1])
test5([1])
print(test5.__defaults__)
print(test4.__defaults__)


def bar(xyz,a=2,b='abd',c=(4,),*args,m=4,n=4,**kwargs):
    pass

print(bar.__defaults__)
print(bar.__kwdefaults__)

print("函数的销毁----------------------------")
'''
函数的销毁
    记住，函数也是对象，所以重新声明之后，就是一个新的对象了
    使用del
'''
def foo(xyz=[],u='abc',z=123):
    xyz.append(2)
    print(xyz)
    return xyz

print(foo(),id(foo),foo.__defaults__)

def foo(xyz=[],u='abc',z=123):
    xyz.append(2)
    print(xyz)
    return xyz

print(foo(),id(foo),foo.__defaults__)
z = foo
z()

del foo#这也说明del只是在让一个对象被引用的计数器-1，垃圾回收器到底回不回收就要看这个对象的引用计数器是否为0了
print('---------------------------')
print(z(),id(z),z.__defaults__)
print("-------------------")

#函数也是对象，当使用del之后，那么这个对象对应的变量名就会被删除
#print(foo(),id(foo),foo.__defaults__)















