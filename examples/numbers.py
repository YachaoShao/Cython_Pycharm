#!/usr/local/bin/python
# -*- coding: UTF-8 -*-

# # example1
# d = []
# for i in range(1, 5):
#     for j in range(1, 5):
#         for k in range(1, 5):
#            # if(i != j) and (i != k) and (j != k):
#             if i != j != k:
#                 d.append([i*100+j*10+k])
# print(len(d))
# print(d)

# example 2

# income = int(input("Profit of this month:"))
#
# if income <= 10000:
#     Awards = income*0.1
# elif income <= 20000:
#     print("The award for 10000:", 1000)
#     Awards = (income-10000)*0.075+ 1000
# elif income <=40000:
#     print("The award from 10000 to 20000:", 1750)
#     Awards = (income-20000)*0.05 + 10000*0.075 +1000
# print("The total awards is:", Awards)

# income = int(input("Profit:"))
# dif = [1000000, 600000, 400000, 200000, 100000, 0]
# rat = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
# Award = 0
# for idx in range(0, 6):
#     if income > dif[idx]:
#         interst = (income-dif[idx])*rat[idx]
#         Award = Award + interst
#         print("The award for the part over ", dif[idx], " is ", interst)
#         income = dif[idx]
# print("The total award is:", Award)

# example date
#
# year = int(input("year:\n"))
# month = int(input("month:\n"))
# day = int(input("day:\n"))
# sum = 0
# days =(0, 31, 59, 90, 120, 151, 180, 212, 243, 273, 304, 334)
#
# if ((year % 100 == 0) or (year % 4 ==0)) and (year % 100 != 0) and month>2:
#     sum = days[month-1] + day +1
# else:
#     sum = days[month-1] + day
#
# print("This is the", sum, "th day.\n")
class ManInBlack:
    " Historical Man "
    Number = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        ManInBlack.Number += 1

    def displayNumber(self):
        print("Number of Man In Black ", ManInBlack.Number)

    def displayManInBlack(self):
        print("Name: ", self.name, ", age:", self.age)

ManInBlack1 = ManInBlack("Smith", 22)
ManInBlack2 = ManInBlack("Will", 24)

ManInBlack1.displayManInBlack()
ManInBlack2.displayManInBlack()
ManInBlack2.displayNumber()

