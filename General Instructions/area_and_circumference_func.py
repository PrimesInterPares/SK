# -*- coding: utf-8 -*-
import numpy as np

r = input(u'Input radius: ')

def length(r):
    c = 2*np.pi*r
    print "circle's length = %.3f" % (c)

    
def square(r):
    s = np.pi*r**2
    print "circle's square = %.3f" %(s)
length(r)
square(r)