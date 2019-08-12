# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 04:36:32 2019

@author: aot
"""

a,b={int(i) for i in input("Enter two number :").split()}
max=a if (a>b) else b
print("Max Number among two is {}".format(max))