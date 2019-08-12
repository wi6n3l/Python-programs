# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 05:49:43 2019

@author: aot
"""

row=int(input("Enter the number of rows:"))
c=1
for i in range(1,row+1):
    for j in range(1,i+1):
        print(c,end=" ")
        c=c+1
    print()