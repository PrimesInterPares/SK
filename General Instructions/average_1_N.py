# -*- coding: utf-8 -*-


n = input(u'Input number more then 1: ')

def average(n):
    sum = 0
    for i in range(n+1):
        sum += i
    average = float(sum)/n
    print "Average of %.d numbers = %.1f" % (n, average)

average(n)