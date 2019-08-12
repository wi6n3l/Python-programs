# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 05:55:10 2019

@author: aot
"""

a=[int(i) for i in input("Enter the tuple:").split()]
a=tuple(a)
ar=set(a)
for i in ar:
    if(a.count(i)>1):
         print(i,end=" ")