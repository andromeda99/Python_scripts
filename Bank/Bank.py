'''
Created on Aug 1, 2016

@author: Aamir
'''
from OOP.Bank_menu import menu, balance, exitt, withdr, dep, incr
Mymenu = menu()
Mybal=balance()
Mywithdraw=withdr()
Mydep=dep()
Myincr= incr()
Myexit=exitt()
n=1
m=1
print('### Members please enter Diners Club Card Passphase ### ')
for x in range(0,4):
    x = str(input('Please enter your password:- '))
    flag=0
    n+=1
    if (x =='****'):
            flag = 1
            break
    elif (n==4):
                print ('You have exceeded no. of attempts. Please visit branch')
                print ('***Please renew your PIN***')
                flag=0
                break 
    else:
         print ('Please enter correct password:- ')
               

if flag==1:
    while True:
        if m==2:
            break
        else:
            print('1. Silver Card')
            print('2. Gold Card ')
        
            x=input('Please enter S/s for Silver or G/g for Gold Card:- ')
         
        if x=='S' or x=='s':
            while True: 
                if m==2:
                    break
                else:
                    try:
                        Mymenu.menulist()
                        x=int(input('Please enter your choice:- '))
                    except Exception:
                            print('***Please enter Numeric value as mentioned above***')
                            continue
                    if x==1:
                        Mybal.bal()
                        z=input('Press Y/y for Banking options or N/n to exit:- ')
                        if z=='y' or z=='Y':
                            continue
                        else:
                            print ('Thanks for using Diners Club bank')
                            m=2
                            break
                    elif x==2:
                        Mywithdraw.withdraw()  
                    elif x==3:
                        Mydep.deposit()
                    elif x==4:
                        Myincr.increase()
                        z=input('Press Y/y for banking options or N/n to Exit:- ')
                        if z=='Y' or z=='y':
                            continue
                        else:
                            print ('Thanks for using Diners Club bank')
                            m=2
                            break
                    elif x==5:
                        m=2
                        Myexit.exit()
                        break
                    else:   
                        print('Invalid option...Please try again....')
                        continue
        
    