#!/usr/bin/python
#Cheechee Lin PIC 97 HW 1 01/07/2016 
#Newton's Method for given test cases 

import math

#hardcoded functions and their derivatives 
def f(x):
	return x**2-1
def df(x):
	return 2*x-1
def g(x):
	return math.sin(x)
def dg(x):
	return math.cos(x)
def h(x):
	return math.log1p(x-1)-1
def dh(x):
	return 1/x

#Newton's Method 
def newton(func,dfunc,x,eps):
	xi=x
	#if magnitude of residual error is less than or equal to eps then done, else calculate correction to guess
	while math.fabs(func(xi))>eps:
		xi= xi-float(func(xi)/dfunc(xi))
		if math.fabs(func(xi)-func(x))<=eps:
			break
	return xi


print newton(f,df,3,0.0001)
print newton (f,df,-0.5,0.0001)
print newton (g,dg,2,0.0001)
print newton (h,dh,1.5,0.0001)