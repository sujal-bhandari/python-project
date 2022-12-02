'''You task is to replicate the working of ATM for a single user, let’s say,
 Mr. John, who has already successfully logged into her account on the ATM Machine, now,
 we will program the next steps he may want to perform. 
Like display his name and cash available in his savings account
Withdraw cash and display the status of the cash balance.
Deposit cash and display the status of the cash balance.
(Your task is to design and implement the ATM functionality by taking care of all constraints,
 for example if minimum cash available is less than 5000 then system will display low balance)'''

import time

print("Please insert Your CARD")

# for card processing
time.sleep(2)
password = 4321

# taking atm pin from user
pin = int(input("Enter your ATM pin: "))


# checking pin is valid or not
if pin == password:
    #shows name of the owner
    print("Welcome Mr.John")
    # loop will run user get free

    #user account balance
    balance =10000
        #loop will run user get free 
    while True:

            #Showing  info to user

        print(""" 
                            1 == balance
                            2 == withdraw balance
                            3 == deposit balance
                            4 == exit
                            """
                  )

        try:    
                 #taking an option from user
            option = int(input("Please enter your choice: "))
        except:
            print("Please enter valid option")
            
            #for option 1        
        if option == 1:
            print(f"Your current balance is: {balance}")
                                         
        if option == 2:

            withdraw_amount = int(input("please enter withdraw_amount: "))

                

            balance = balance - withdraw_amount

            print(f"{withdraw_amount} is debited from your account")

                

            print(f"your updated balance is: {balance}")

                

        if option == 3:

            deposit_amount = int(input("please enter deposit_amount: "))

            balance = balance + deposit_amount

                

            print(f"{deposit_amount} is credited to your account")



            print(f"your updated balance is: {balance}")

        if balance<5000:
            print("Low Balance")



        if option == 4:

            break
else:
    print("Wrong Pin")

