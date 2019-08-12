# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 06:12:13 2019

@author: aot
"""

row=int(input("Enter the number of rows:"))
c=65
for i in range(1,row+1):
    for j in range(0,i):
        print(chr(c+j),end=" ")
    print()