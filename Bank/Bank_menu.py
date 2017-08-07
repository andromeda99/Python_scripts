'''
Created on Aug 1, 2016

@author: Aamir
'''
#@from OOP.ATM import Mywith


class menu():
    def menulist(self):
        print('***Welcome to Diners Club Silver Card***')
        #print('### Please select from below options ###')
        print('1. Balance inquiry')
        print('2. Withdrawal')
        print('3. Deposit')
        print('4. Increase Limit')
        print('5. Exit')
        
        
        
        
        
class balance():
        balance=50000
        def bal(self):
            print('Your current & available balance is Rs/- {0}' .format(balance.balance))
        

class withdr():
    y=0
    def withdraw(self):
        m=0
        n=0
        x=0
        while True:
            if m==1:
                break
            elif (balance.balance == 0):
                print('You have insufficient funds in your account')
                break
                m=1
            else:
              if n==3:
                print('Too many withdrawal attempts...Please try again')
                break
              else:
                while n!=3:
                    try:
                        x=float(input('Please enter Withdrawal Amount:- '))
                    except Exception:
                        print('***Withdrawal Amount should be Numeric***')
                        break
                    if (x < 100):
                        print('Minimum denomination is Rs/- 100')
                        n+=1
                        break
                    elif (x > balance.balance):
                        print('Amount exceeds available Balance')
                        n+=1
                        break
                    elif x%50!=0:
                        print('Please enter multiples of 100`s & above')
                        n+=1
                        break
                    else:
                            balance.balance = (balance.balance) - (x)
                            print('Your available balance after withdrawal is Rs/- {0}' .format(balance.balance))
                            withdr.y+=1
                            z=input('Press Y/y to withdraw more funds or N/n for other options:- ')
                            
                            if z=='y' or z=='Y':
                                continue
                            else:
                                m=1
                                break
                    

class dep():
    def deposit(self):
        m=0
        n=0
        while True:
          if m==1:
              break
          else:
            if n==3:
                print('Too many incorrect deposit attempts...Please try again...:-')
                break
            else:
              while (n!=3):  
                x=float(input('Please enter amount to deposit:- '))
                if x<=99:
                    print('Please enter Multiples of 100`s & above ')
                    n+=1
                    break
                elif x%50!=0:
                    print('Unacceptable Amount...Please enter an Even round figure...')
                    n+=1
                    break                
                else:
                    balance.balance=(x) + balance.balance
                    print('Your current & available balance after Deposit is Rs/- {0}' .format(balance.balance))
                    n=0
                    withdr.y+=1
                    z=input('Press Y/y for more Deposits or N/n for other Banking options:- ')
                    if z=='Y' or z=='y':
                        continue
                    else:
                        m=1
                        break

class incr():
    def increase(self):
        
            print('***Welcome to Diners Club Silver Credit Card***')
            if withdr.y == 1:
                print('You have earned 100 points due to your transaction')
                print('You are eligible to get your Limit increased upto 1000 Rs/- ')
                z=input('Press Y/y to increase your limit or N/n to exit:- ')
                if z=='Y' or z=='y':
                    balance.balance = balance.balance + 1000
                    print('!!! Congratulations !!! Your Limit has been increased')
                    print('Your current & available balance is Rs/- {0}' .format(balance.balance))
                else:
                    return
            elif withdr.y == 2:
                print('You have earned 500 points due to your transaction')
                print('You are eligible to get your Limit increased upto 3000 Rs/- ')
                z=input('Press Y/y to increase your limit or N/n to exit:- ')
                if z =='Y' or z=='Y':
                    balance.balance = balance.balance + 3000
                    print('!!! Congratulations !!! Your Limit has been increased')
                    print('Your current & available balance is Rs/- {0}' .format(balance.balance))
                else:
                    return
            elif withdr.y == 3:
                    print('You are eligible to get your Limit increased upto 5000 Rs/- ')
            
            else:
                print('### You are not eligible for any upgradation in your limit ###')
                print('Please undergo few transaction in your account & then apply for the Upgrade')
            
            
            

        
class exitt():
    def exit(self):
        print ('*** Thanks for using Diners Club Silver Card*** ***')
        SystemExit
        
        