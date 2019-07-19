# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 09:48:18 2019

@author: SWANMOY
"""

def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
def combi(n, r):
    g=fact(n)/(fact(n-r)*fact(r))
    return g
x, s, y, m, z, c=input().split()
x=int(x)
s=int(s)
y=int(y)
m=int(m)
z=int(z)
c=int(c)
ch1, ch2=input().split()
ch3=input()
c1=ord(ch1)-64
c2=ord(ch2)-64
c3=ord(ch3)-64
result1=combi(x, s)*combi(y, m)*combi(z, c)
print(result1)
x1=x
y1=y
z1=z
s1=s
m1=m
c4=c
u2=x+y
if c3>=1 and c3<=x:
    x1-=1
elif c3>x and c3<=u2:
    y1-=1
else:
    z1-=1
result2=combi(x1, s1)*combi(y1, m1)*combi(z1, c4)
if c1>=1 and c1<=x:
    x1-=1
    s1-=1
elif c1>x and c1<=u2:
    y1-=1
    m1-=1
else:
    z1-=1
    c4-=1
if c2>=1 and c2<=x:
    x1-=1
    s1-=1
elif c2>x and c2<=u2:
    y1-=1
    m1-=1
else:
    z1-=1
    c4-=1
result3=combi(x1, s1)*combi(y1, m1)*combi(z1, c4)
result4=result2-result3+1
print(result4)
