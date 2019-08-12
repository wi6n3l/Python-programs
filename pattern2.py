# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 05:54:19 2019

@author: aot
"""

row=int(input("Enter the number of rows:"))
c=65
for i in range(1,row+1):
    for j in range(1,i+1):
        print(chr(c),end=" ")
        c=c+1
    print()