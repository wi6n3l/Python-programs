# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 04:53:12 2019

@author: aot
"""

row=int(input("Enter the number of rows:"))
for i in range(1,row+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
