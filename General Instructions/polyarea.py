# -*- coding: utf-8 -*-


x = [2,4,9,3]
y = [1,0,3,6]

def square(x,y):
    s = 0
    length = len(x)
    for i in range(length):
        if i+1 < length:
            s += (x[i]+x[i+1])*(y[i]-y[i+1])
        else:
            s += (x[i]+x[0])*(y[i]-y[0])
    print "Polygon's square = %.f" %(s/2)

    
square(x,y)