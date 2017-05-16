'''
Created on Jul 14, 2016

@author: LAB207
'''
print 'Function to print a table'

val = input('Please enter any number:- ')

def table( val ):
        for x in xrange(1,11):
            print x*val
            
            
            

table(val)

