# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 06:28:56 2019

@author: aot
"""

a=[int(i) for i in input("Enter the tuple:").split()]
a=tuple(a)
d={}
for i in range(0,len(a)):
    d[i]=a[i]
print(d)