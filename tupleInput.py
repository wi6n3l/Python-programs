# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 04:40:44 2019

@author: aot
"""

a=[int(i) for i in input("Enter the tuple:").split()]
a=tuple(a)
for i in a:
    print (i,end=" ")
a=list(a)
el=int(input("Enter the element to insert:"))
a.append(el)
a=tuple(a)
for i in a:
    print (i,end=" ")
print(type(a))
    
