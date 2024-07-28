a="Welcome : "
Available_Amount = 1000
card = input("Enter Card Name : ")
PIN = input("Enter PIN Number : ")
while True:
    if len(PIN)==4:
        print(a,card)
        print("----Select Your Transaction----")
        print("1. Withdraw")
        print("2. Check Balance")
        print("3. Deposit")
        print("4. Exit")
    else:
       print("Please Check PIN Number")
       break
    Option = input("Select Option : ")

    if Option == "1" or Option == "Withdraw":
        Amount = int(input("Enter the withdraw amount: "))
        if Amount > Available_Amount:
            print("Insufficient Balance")
        else:
            Available_Amount -= Amount
            print(f" Rs. {Amount:.2f}  withdraw. Balance is Rs. {Available_Amount:.2f}")
    elif Option == "2" or Option== "Balance":
        print(f"Your balance is Rs. {Available_Amount:.2f}")
    elif Option == "3" or Option=="Deposit":
        Deposit_Amount = int(input("Enter the Deposit amount: "))
        if Deposit_Amount <= 0:
            print("Enter Valuable Amount")
        else:
            Available_Amount += Deposit_Amount
            print(f" Rs. {Deposit_Amount:.2f}  Debited. Balance is Rs. {Available_Amount:.2f}")
    elif Option == "4" or Option== "Exit" :
        print(" Your Transaction is Complete \n Please Take Your Cash \n Thank You For Visiting our ATM")
        break
    else:
        print("Invalid Selection")