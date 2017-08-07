'''
Created on Jul 18, 2016

@author: Aamir
'''


n=1
print ('Welcome to Jhol ATM')
for x in range(0,4):
    x = input('Please enter your password:- ')
    
    n+=1
    if (x =='****'):
            print ('***Welcome to net banking***')
            flag = 1
            break
    elif (n==4):
                print ('You have exceeded no. of attempts. Please visit branch')
                print ('***Please renew your PIN***')
                flag = 0
                break 
    else:
         print ('Please enter correct password:- ')
         continue
     

Myatmopt = atmoptions()
Myatmfunct = atmfunctions()
Myexit = exitt()
Mymini=mini()
Mywith=withdr()


if flag == 1:
    #Myatmopt.opt()
    while True:
        Myatmopt.opt()
        x=int(input('Enter your choice: '))
        if (x==1):
            Myatmfunct.bal()
            z=input('Press Y/y for Banking options N/n to exit:- ')
            if z=='y' or z=='Y':
                continue
            else:
                print ('Thanks for using Jholer bank')
                break
        if (x==2):
            Mymini.state()
            z=input('Press Y/y for Banking options N/n to exit:- ')
            if z=='y' or z=='Y':
                continue
            else:
                print ('Thanks for using Jholer bank')
                break
        elif (x==3):
            Mywith.drw()
            z=input('Press Y/y for Banking options N/n to exit:- ')
            if z=='y' or z=='Y':
                continue
            else:
                print ('Thanks for using Jholer bank')
                break
        elif (x==4):
            Myexit.exit()
            
            break
        else:
           continue
    else:
    #print ('*** Your Card has been blocked ***')
        pass

    
    


    





    
           
     
   
