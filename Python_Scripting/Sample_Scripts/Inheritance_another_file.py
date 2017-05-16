'''
Created on Jul 15, 2016

@author: LAB207
'''
from OOP.class_object2 import Operations
class Display(Operations):
        def Odd(self):
            print 'Hi this is inheritance'

Myobjectz = Display()
print 'Calling Object from Another File'
print '==============================='
Myobjectz.Addition()