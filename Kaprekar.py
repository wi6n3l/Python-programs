# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 23:28:09 2019

@author: swapn
"""

def checkIsKaprekar( num ):
    string_num = str(num**2)
    if num == int(string_num[:len(string_num)//2]) + int(string_num[len(string_num)//2:]):
        return True

kaprekars = [ str(i) for i in range(int(input("Enter Lower Value: ")),int(input("Enter Upper Value :"))) if checkIsKaprekar(i) == True ]
print (' '.join(kaprekars))