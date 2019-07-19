# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 21:44:16 2019

@author: swapn
"""

a=int(input("Enter the number 1: "))
b=int(input("Enter the number 2: "))
c=int(input("Enter the number 3: "))
if(a>b)and(a>c):
    print("The first number {} is largest of all".format(a))
elif(b>a)and(b>c):
    print("The second number {} is largest of all".format(b))
else:
    print("The third number {} is largest of all".format(c))