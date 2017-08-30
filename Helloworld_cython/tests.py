#!/usr/bin/python
# -*- coding: UTF-8 -*-
print "hello world"


list1 =['sky', 10, 'math', 90 ]
print list1

print list1[1:2]*2


dict = { }
dict['one'] = "This is one"
dict[2] = "This is two"

tinydict = {'name':'john','code':13121,'dept':'sales'}

print dict['one']
print dict[2]
print tinydict
print tinydict.keys()
print tinydict.values()

a = 10
b = 20
list = [1, 2, 3, 4, 5]

if (a in list):
    print "1 - 变量 a 在给定的列表中 list 中"
else:
    print "1 - 变量 a 不在给定的列表中 list 中"

if (b not in list):
    print "2 - 变量 b 不在给定的列表中 list 中"
else:
    print "2 - 变量 b 在给定的列表中 list 中"

# 修改变量 a 的值
a = 2
if (a in list):
    print "3 - 变量 a 在给定的列表中 list 中"
else:
    print "3 - 变量 a 不在给定的列表中 list 中"

a=10
b=10

print a is b


if a is not b:
    print "a and b has not same xaddress"
else:
    print "a and b has same xaddress"

