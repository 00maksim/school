name = ""   #account name variable
balance = 0.0   #account balance variable

while True:
    print(" -Simple Banking System- ") #lines for options: 1 for new account, 2 for deposit money, 3 for withdraw money, 4 for checking balance, 5 to exit
    print("1. Create a New Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")

    # Create a New Account
    if choice == "1": #when 1 is typed in console
        print(" -Create a New Account- ")   
        name = input("Enter your name: ")   # enter name for account
        balance = float(input("Enter your initial balance: ")) #cast the user input balance to float value
        print(f"Account created successfully for {name} with an initial balance of ${balance:.2f}.") #round balance to 2 decimals

    # Deposit Money
    elif choice == "2":
        if name:  # Check if account exists
            print(" -Deposit Money- ")  
            amount = float(input("Enter the amount to deposit: ")) #set a variable amount to be the amount to deposit
            if amount > 0:  #check if amount is greater than 0 for it to be true
                balance += amount   # add amount into balance
                print(f"${amount:.2f} deposited successfully. New balance: ${balance:.2f}") #message for sucessfully deposit with balance rounded to 2 decimals
            else:
                print("Invalid deposit amount. Enter a proper value") #if deposit amount is negative or 0 it is invalid
        else:
            print("Create an account first") #if no account print this line

    # Withdraw Money
    elif choice == "3":
        if name:  # Check if account exists
            print(" -Withdraw Money- ")
            amount = float(input("Enter the amount to withdraw: ")) #set a variable amount to be the amount to withdraw
            if amount > 0: #check if amount is greater than 0 for it to be true
                if amount <= balance: # check if amount is less than balance for the user to successfully withdraw the amount
                    balance -= amount # subtract amount from balance
                    print(f"${amount:.2f} withdrawn successfully. New balance: ${balance:.2f}")
                else:
                    print("Insufficient funds. Withdrawal failed.") # prints this line if the amount trying to withdraw is more than balance
            else:
                print("Invalid withdrawal amount. Enter a proper value") #if withdraw amount is negative or 0 its invalid
        else:
            print("Please create an account first.") #if no account print this line

    # Check Balance
    elif choice == "4":
        if name:  # Check if account exists
            print(" -Check Balance- ")
            print(f"Account balance for {name}: ${balance:.2f}") # check balance
        else:
            print("Please create an account first.") # print this line if no account exists

    # Exit the Program
    elif choice == "5":
        print("Exiting......")
        break
