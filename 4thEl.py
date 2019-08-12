# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 05:47:12 2019

@author: aot
"""

a=[int(i) for i in input("Enter the tuple:").split()]
a=tuple(a)
print (a)
print ("The 4th element is {} and 4th last element is {}".format(a[3],a[len(a)-4]))