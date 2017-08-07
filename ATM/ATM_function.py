'''
Created on Jul 19, 2016

@author: Aamir
'''


class atmfunctions():
        balance = 8000
        def bal(self):
            
                print ('Your current & available balance is Rs/- {0}' .format(atmfunctions.balance))
                return
                
                
                
class mini():
        def state(self):
            
                print ('1. Your Last transaction was a Balance Inquiry')
                print ('2. Your Last transaction was a Withdrawal')
                return
            
            
            
            
class withdr():
        def drw(self):
            while True:
                print ('Your Balance is Rs/- {0}' .format(atmfunctions.balance))
                x=float(input('Please enter withdrawal amount:- '))
                if x > atmfunctions.balance:
                    print ('Amount exceeds avail. bal:- ')
                else:
                    atmfunctions.balance = (atmfunctions.balance) - (x) 
                    print ('Your Balance is Rs/- {0}' .format(atmfunctions.balance))
                    if atmfunctions.balance == 0:
                            print ('You have insufficient funds in your account')
                            print ('Your balance is Rs/- {0}' .format(atmfunctions.balance))
                            break
                    else:
                        z=input('Do you wish to continue. Press Y/y to continue or N/n to exit:- ')
                    if z=='y' or z=='Y':
                        if atmfunctions.balance == 0:
                            print ('You have insufficient funds in your account')
                            break
                        else:
                            continue
                    else:
                        print ('Thanks for using Withdrawal utility:- ')
                        break

class exitt():
            def exit(self):
                    print ('*** Thanks for using Jholer ATM. Wish to see you again ***')
                    SystemExit
                




