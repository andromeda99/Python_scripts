'''
Created on Jul 15, 2016

@author: LAB207
'''
class Myclass:
        val = 99
        def funz(self):
            a=9
            b=3
            c=a+b
            return c
    
Myobject = Myclass()
print Myobject.val
res = Myobject.funz()
print res
