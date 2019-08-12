# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 05:03:02 2019

@author: aot
"""
c=input("Enter the choice(C or F):")
temp=int(input("Enter the temperature:"))
if(c=="C"):
    result=((9*temp)/5)+32
    print("The temperature is ={} F".format(result))
elif(c=="F"):
    result=((temp-32)*5)/9
    print("The temperature is ={} C".format(result))
else:
    print("Invalid")