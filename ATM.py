
import time 
#for stopping program execution for some time
print("Please insert you card")
#for card processing
time.sleep(5)

#taking atm pin from user
password = 123456

pin = int(input("Enter you ATM Pin "))

balance = 5000
#checking pin is valid or not 
if pin == password:

   while True:
    #Showing  info to user
    print("""
              1. Balance
              2. Withdraw Amount 
              3. Deposit 
              4. Exit
          """)
    try: 
        option=int(input("Please enter you option"))
    except: 
        print("Please enter valid option")
     #for option 1        
    if option==1:
        print(f"Your current balance is {balance} ")
     #for option 2       
    if option==2: 
        withdraw_amount=int(input("Please enter you withdraw_amount" ))
        balance=balance=withdraw_amount

        print(f"{withdraw_amount} is debited your account")

        print(f"Your updated balance {balance}")
     #for option 3
    if option==3:
        deposit_amount=int(input("Please enter deposit_amount" ))
        balance=balance+deposit_amount

        print(f"{deposit_amount} is credited to your account ")
        print(f"Your updated balance is {balance} ")
    #Exit
    if option==4:
        break
        
else: 
    print("Wrong pin Please try again")