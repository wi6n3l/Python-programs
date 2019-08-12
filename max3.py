# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 05:10:34 2019

@author: aot
"""

a,b,c=[int(i) for i in input("Enter three number :").split()]
max=a if (a>b)and(a>c) else b if (b>c) else c
print("Max Number among the three is {}".format(max))