'''
Created on Jul 26, 2016

@author: Aamir
'''

bal = 1000
while True:
    print ('Your Balance is Rs/- {0}' .format(bal))
    x=float(input('Please enter withdrawal amount:- '))
    if x > bal:
        print ('Amount exceeds avail. bal:- ')
    else:
            bal = (bal) - (x)
            print ('Your Balance is Rs/- {0}' .format(bal))
            z=input('Do you wish to continue. Press Y/N')
            if z=='y' or z=='Y':
                continue
            else:
                print ('Thanks for using Jholer bank')
                break
            