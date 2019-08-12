# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 06:39:19 2019

@author: aot
"""

a=[int(i) for i in input("Enter the tuple:").split()]
a=tuple(a)
print("The original Tuple: ",a)
a=list(a)
a.reverse()
a=tuple(a)
print("The reversed Tuple",a)