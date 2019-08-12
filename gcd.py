# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 20:08:37 2019

@author: swapn
"""

a,b=[int(i) for i in input("Enter two numbers:").split()]
while(b):
    a,b=b,a%b
print("The gcd is {}".format(a))