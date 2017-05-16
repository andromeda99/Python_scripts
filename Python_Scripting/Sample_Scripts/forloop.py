'''
Created on Jul 13, 2016

@author: LAB207
'''
primes = [2, 3, 5, 7]
for p in primes:
    print p
    

print '***********************************************'
n = 2
for x in xrange(1,11): # or range(5)
    print x*n

print '***********************************************'
count = 1
n=2
while (count <= 10):
    t=n*count
    print t
    count+=1
print '***********************************************'

val = input('Please enter your Value:- ')
print val
count = 1
while (count <= 10):
    t=val*count
    print t
    count+=1
print '***********************************************'

for x in xrange(1,11): # or range(5)
    print x*val
    


 

    
    

        