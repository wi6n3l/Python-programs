# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 05:59:51 2019

@author: aot
"""

a=[int(i) for i in input("Enter the tuple:").split()]
a=tuple(a)
s=int(input("Enter the element to search: "))
if(a.count(s)>0):
    print("Found !!")
else:
    print("Not Found !!")