# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 05:47:22 2019

@author: aot
"""
import math
arr=[]
for a in range(0,5):
    arr.append(int(input("Enter the number:")))
print(arr)
for a in arr:
    print(a,end=" ")
print(math.sqrt(a))