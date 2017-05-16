'''
Created on Jul 14, 2016

@author: LAB207
'''

a = input('Please enter val a:- ')
b = input('Please enter val b:- ')

#Simple function
def add(a,b):
    print 'Addition of a & b is {0}' .format(a+b)
    
add(a, b)

#Call by value function
def add(a,b):
    c = a + b
    return c

res = add(a,b)
    
print res



