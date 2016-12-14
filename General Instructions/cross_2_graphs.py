# -*- coding: utf-8 -*-
import math
import numpy as np


n = input(u'Input number: ')
e = float(input(u'Input error: '))

x = np.linspace(-4,4,n)
solution = []

for i in range(len(x)):
    if math.fabs(x[i]-x[i]**2) < e:
        solution.append(x[i])
        
for i in range(len(solution)):
    print 'Solutions : x = %.f' %(solution[i])