user_pin = 2109
user_balance = 115000.50
user_name = "santhosh kumar"
print("Welcome to ATM ", user_name, end = "\n")

choice = 9

while (True):
    print(" Logout and Exit")
    print(" View Account Balance")
    print(" Withdraw Cash")
    print(" Deposit Cash")
    print(" Change PIN")
    print(" Return Card")
    choice = int(input("Enter number to proceed :\n"))

    if choice == 0:
        print("Exiting...")
        print("You have been logged out. \n Thank you")
    

    elif choice in (1,2,3,4,5):
        num_of_tries = 3
        while (num_of_tries!=0):
            input_pin = int(input("Please enter your 4-digit PIN :"))

            if input_pin == user_pin:
                print("Account auhtorized\n")

                if choice == 1:
                    print("Loading Account Balance...")
                    print("Your current balance is Rs.", user_balance, end = "\n")
                
                elif choice == 2:
                    print("Opening Cash Withdrawal...")
                

                    while(True):
                        withdraw_amt = float(input("Enter the amount you wish to withdraw > "))

                        if withdraw_amt>user_balance:
                            print("Can't withdraw Rs.", withdraw_amt)
                            print("Please enter a lower amount:")
                            continue

                        else:
                            print("Withdrawing Rs.", withdraw_amt)
                            confirm = input("Confirm: Yes/no > ")
                            if confirm in ('Yes', 'yes'):
                                user_balance-=withdraw_amt
                                print("Amount withdrawn - Rs.", withdraw_amt)
                                print("Remaining balance - Rs.", user_balance, end = "\n")
                                break

                            else:
                                print("Cancelling transaction...")
                                print("Transaction Cancelled!\n")
                                break

                elif choice == 3:
                    print("Loading Cash Deposit...")

                    deposit_amt = float(input("Enter the amount you wish to deposit > "))
                    print("Depositing Rs.", deposit_amt)
                    confirm = input("Confirm: yes/No ")
                    if confirm in ('Yes', 'yes'):
                        user_balance+=deposit_amt
                        print("Amount deposited - Rs.", deposit_amt)
                        print("Updated balance - Rs.", user_balance, end = "\n")
                    else:
                        print("Cancelling transaction...")
                        print("Transaction Cancelled!\n")

                elif choice == 4:
                    print("Loading PIN Change...")
                
                    pin_new = int(input("Enter your new PIN > "))

                    print("Changing PIN to", pin_new)
                    confirm = input("Confirm: Yes/No: ")
                    if confirm in ('Yes', 'yes'):
                        user_pin = pin_new
                        print("PIN changed successfully \n")
                    else:
                        print("Cancelling PIN change...")
                    

                else:
                    print("Returning your ATM Card")
                    confirm = input("Confirm:Yes/No ")
                    if confirm in ('Yes', 'yes'):
                        print("Card returned successfully!\n")
                    else:
                        print("Process Cancelled!\n\n")

                    break

            else:
                num_of_tries-=1
                print("PIN incorrect! Number of tries left -", num_of_tries, end = "\n")

        else:
            print("Exiting...")
        
            print("You have been logged out.\n\n\n Thank you!\n")
            


    else:
        print("Invalid input!")
        print(" Enter 0 to Logout and Exit!")
