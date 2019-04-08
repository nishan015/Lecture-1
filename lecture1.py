# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
print("this is a corrected test phrase")

# Lecture 1 Variables and Data Types
a = 5 # is a integer type
b = 5.1 # this is a float type
c = "Hello World" #this is a string
d, e = True, False #two assignements together, one should avoid such assignments
f = None

z = a # no new memory location created but is same as 'a'
a is z # checking if a and z are stored in the same location, or to say are these same objects

type(a)

w = 5
u = 5
w is u # this is a result of memory optimisation. The output will be true

t = 500
y = 500
t is y  # this will throw up false because it is not optimised

