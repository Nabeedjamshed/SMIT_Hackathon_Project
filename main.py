from bank import Bank
def main():
    bank = Bank()
    print()
    print("*******Welcome to the Banking System*******")
    while True:
        print("\n1. Open Account")
        print("2. Login to Account")
        print("3. Admin: View Total Deposits")
        print("4. Admin: Check Total Accounts")
        print("5. Exit")
        key1 = int(input("Enter your key: "))

        if key1 == 1:
            account_holder = input("Enter account holder name: ")
            account_type = input("Enter account type (savings/current): ").lower()
            username = input("Set a username: ")
            password = input("Set a password: ")
            if len(password) < 8:
                print("Password should be at least 8 characters long.")
            elif password.isalpha():
                print("Password should contain at least one number.")
            elif password.isnumeric():
                print("Password should contain at least one letter.")
            elif password.islower():
                print("Password should contain at least one uppercase letter.")
            elif password.isupper():
                print("Password should contain at least one lowercase letter.")
            elif password.isalnum():
                print("Password should contain at least one special character.")
            else:
                bank.open_account(account_holder, account_type, username, password)
        elif key1 == 2:
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            
            account = bank.authenticate_user(username, password)
            if account:
                print(f"\nWelcome, {account.account_holder}!")
                while True:
                    print("\n1. Deposit Money")
                    print("2. Withdraw Money")
                    print("3. Check Balance")
                    print("4. Print Statement")
                    print("5. Calculate Interest")
                    print("6. Transfer Money")
                    print("7. Logout")
                    key2 = int(input("Enter your key: "))
                    if key2 == 1:
                        amount = float(input("Enter amount to deposit: "))
                        account.deposit(amount)
                    elif key2 == 2:
                        amount = float(input("Enter amount to withdraw: "))
                        account.withdraw(amount)
                    elif key2 == 3:
                        print(f"Current balance: {account.check_balance()}")
                    elif key2 == 4:
                        account.print_statement()
                    elif key2 == 5:
                        if account.account_type == "savings":
                            interest_rate = float(input("Enter interest rate (%): "))
                            account.calculate_interest(interest_rate)
                        else:
                            print("Interest calculation is not available for current accounts.")
                    elif key2 == 6:
                        receiver_account_number = int(input("Enter receiver's account number: "))
                        amount = float(input("Enter amount to transfer: "))
                        bank.transfer(account.account_number, receiver_account_number, amount)

                    elif key2 == 7:
                        print("Logged out successfully!")
                        break
                    else:
                        print("Invalid key. Please try again.")
            else:
                print("Authentication failed. Invalid username or password.")
        elif key1 == 3:
            print(f"Total deposits in the bank: {bank.admin_check_total_deposit()}")
        elif key1 == 4:
            print(f"Total number of accounts in the bank: {bank.admin_check_total_accounts()}")
        elif key1 == 5:
            print("Exiting the banking system. Have a good day!")
            break
        else:
            print("Invalid key. Please try again.")


if __name__ == "__main__":
    main()