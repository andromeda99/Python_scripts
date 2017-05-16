'''
Created on Jul 14, 2016

@author: LAB207
'''
n = input('Please enter any numbeer:- ')
x=n

def fact(x,n):
    while (n!=1):
        x=x*(n-1)
        n-=1
        
    
    return x
        
        
res = fact(x, n)
print res
        
 

    