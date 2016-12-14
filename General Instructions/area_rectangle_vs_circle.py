# -*- coding: utf-8 -*-
import numpy as np
a = 1.3
b = 0
r = 10.6
scircle = np.pi*r**2


while True:
    b += 1
    if scircle <= a*b:
        b -= 1
        break
print(b)