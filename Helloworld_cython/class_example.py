#!/usr/bin/python
# -*-coding: UTF-8 -*-


class Electronic:
    'number of your electronic devices'
    Num_elec = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Electronic.Num_elec +=1

    def dispalycount(self):
        print "Total number of your Electronic device: %d" %Electronic.Num_elec

    def displayElectro(self):
        print "name : ", self.name, ", price : " , self.price

"Input your first device"
ele1 = Electronic("MACBOOK PRO", 1200)
"Input your second device"
ele2 = Electronic("ipad",400)

ele1.displayElectro()
ele2.displayElectro()

ele2.dispalycount()

print "I have %d electronic device" % Electronic.Num_elec

