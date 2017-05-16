'''
Created on Jul 13, 2016

@author: LAB207
'''

for n  in range(1,11):
    if (n % 2 == 0):
        print n
val = input('Please enter your value:- ')
while True:
    print val
    if val % 2 == 0:
        print 'Value is even'
        break
    else :
        print 'Value is odd'
        break
