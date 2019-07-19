Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def print_powers(pwr, *values):
	for v in values:
		print(v**pwr)

		
>>> print_powers(2,3,5)
9
25
>>> print_powers(8,4,5)
65536
390625
>>> a=9
>>> a
9
>>> id(a)
140727152305040
>>> *a
SyntaxError: can't use starred expression here
>>> a=[1,2,3]
>>> a
[1, 2, 3]
>>> *a
SyntaxError: can't use starred expression here
>>> 
