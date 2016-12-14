# -*- coding: utf-8 -*-
from random import randint
n = input(u'Input number : ')

randomNumbers = []
count = 0.

for i in range(n):
    randomNumbers.append(randint(1,6))
    if randomNumbers[i] == 6:
        count += 1
chance = count/n    
print "Count of 6 : %.f" %(count)
print "Chance of 6's precipitation : %.3f" %(chance)
print randomNumbers