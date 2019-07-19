# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 21:38:59 2019

@author: swapn
"""

row=int(input("Enter the number of rows: "))
for i in range(1,row+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()