from datetime import datetime

class BankAccount:
    def __init__(self, account_number, account_holder, account_type, username, password):
        self.account_number = account_number
        self.account_holder = account_holder
        self.account_type = account_type 
        self.username = username
        self.password = password
        self.balance = 0
        self.transactions = []

    def save_transaction_to_file(self):
        try:
            file_name = f"{self.account_holder}.txt"
            with open(file_name, "w") as file:
                for transaction in self.transactions:
                    file.write(f"{transaction}\n")
                file.write(f"Final Balance: {self.balance}\n")
            print(f"Transactions saved to {file_name}")
        except IOError:
            print("Error writing to the transaction file.")

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return

        self.balance += amount
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.transactions.append(f"[{timestamp}] Deposited: {amount}")
        self.save_transaction_to_file()
        print(f"Successfully deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return

        if self.balance < amount:
            print("Insufficient balance for this withdrawal.")
            return

        self.balance -= amount
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.transactions.append(f"[{timestamp}] Withdrew: {amount}")
        self.save_transaction_to_file()
        print(f"Successfully withdrew {amount}. New balance: {self.balance}")

    def calculate_interest(self, interest_rate):
        if self.account_type == "savings":
            interest = self.balance * (interest_rate / 100)
            self.balance += interest
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.transactions.append(f"[{timestamp}] Interest added: {interest}")
            self.save_transaction_to_file()
            print(f"Interest of {interest} added to the account. New balance: {self.balance}")
        else:
            print("Interest is only applicable to savings accounts.")

    def check_balance(self):
        return self.balance

    def print_statement(self):
        if not self.transactions:
            print("No transactions to display.")
            return

        print(f"\nAccount Statement for {self.account_holder}:")
        for transaction in self.transactions:
            print(transaction)
        print(f"Final Balance: {self.balance}")


class Bank:
    def __init__(self):
        self.accounts = {}

    def open_account(self, account_holder, account_type, username, password):
        account_number = len(self.accounts) + 1
        new_account = BankAccount(account_number, account_holder, account_type, username, password) # Object as an attribute(Composition)
        self.accounts[account_number] = new_account
        print(f"Account created for {account_holder} with account number {account_number} and type {account_type}.")

    def authenticate_user(self, username, password):
        for account in self.accounts.values():
            if account.username == username and account.password == password:
                return account
        return None

    def get_account(self, account_number):
        return self.accounts.get(account_number, None)

    def transfer(self, sender_account_number, receiver_account_number, amount):
        sender_account = self.get_account(sender_account_number)
        receiver_account = self.get_account(receiver_account_number)
        if sender_account and receiver_account:
            if sender_account.balance >= amount:
                sender_account.withdraw(amount)
                receiver_account.deposit(amount)
                print(f"Transferred {amount} from account {sender_account_number} to account {receiver_account_number}")
            else:
                print("Insufficient funds in sender's account.")
        else:
            print("Invalid account number(s).")

    def admin_check_total_deposit(self):
        total_deposit = sum(account.balance for account in self.accounts.values())
        return total_deposit

    def admin_check_total_accounts(self):
        return len(self.accounts)