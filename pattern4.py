# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 06:22:34 2019

@author: aot
"""

row=int(input("Enter the number of rows:"))
sp=row
for i in range(1,row+1):
    sp=sp-1
    print(" "*sp+"*"*row)
    