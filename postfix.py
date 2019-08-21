# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 19:01:20 2019

@author: swapn
"""

stack,post=[],[i for i in input("Enter the post fix expression: ").split()]
for i in post:
    if((i=='*')or(i=='/')or(i=='+')or(i=='-')or(i=='%')):
        a=stack.pop()
        b=stack.pop()
        if(i=='*'):   
            stack.append(a*b)
        elif(i=='/'):
            stack.append(a/b)
        elif(i=='+'):
            stack.append(a+b)
        elif(i=='-'):
            stack.append(a-b)
        else:
            stack.append(a%b)
    else:
        stack.append(int(i))
print("The value is : {}".format(stack.pop()))