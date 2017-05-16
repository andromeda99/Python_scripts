'''
Created on Jul 25, 2016

@author: Aamir
'''
class silver():
    silbal = 50000
    print ('1. View balance')
    print ('2. Withdrawal')
    
    for x in range(10):
        def view(self):
                print ('Your Current Balance is Rs/- {0}' .format(silver.silbal))
                
   
        def withdraw(self):
            
                    print ('Your Current Balance is Rs/- {0}' .format(silver.silbal))
                    Wamt=float(input('Please enter Withdrawal Amount:- '))
                    if (Wamt > silver.silbal):
                            print ('Amount exceeds available balance:- ')
                            
                    else:
                            silver.silbal = silver.silbal - (Wamt)
                            print ('Your current & available balance is Rs/- {0}' .format(silver.silbal))
                    
                
        
        
        
Silvercard=silver()
Silvercard.view()
Silvercard.withdraw()
        
        
        
