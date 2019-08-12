# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 06:14:58 2019

@author: aot
"""

a=[int(i) for i in input("Enter the tuple:").split()]
a=tuple(a)
print(a)
a=list(a)
el=int(input("Enter the element to Delete:"))

if(a.count(el)>0):
    del (a[a.index(el)])
else:
    print("Not present")
a=tuple(a)
print(a)
a=dict(a)
print(a)
