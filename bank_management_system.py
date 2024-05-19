import datetime

class Account:
    def __init__(self, name, email, address, account_type, account_number):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.account_number = account_number
        self.balance = 0
        self.transaction_history = []
        self.loans_taken = 0
    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append((datetime.datetime.now(), 'Deposit', amount))
        print(f"Deposited ${amount}. New balance: ${self.balance}")
    def withdraw(self, amount):
        if amount > self.balance:
            print("Withdrawal amount exceeded")
        else:
            self.balance -= amount
            self.transaction_history.append((datetime.datetime.now(), 'Withdraw', amount))
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
    def check_balance(self):
        print(f"Available balance: ${self.balance}")
    def view_transaction_history(self):
        for transaction in self.transaction_history:
            print(transaction)
    def take_loan(self, amount, bank):
        if self.loans_taken >= 2:
            print("Loan limit reached")
        elif not bank.loan_feature:
            print("Loan feature is currently off")
        else:
            self.balance += amount
            bank.total_loan += amount
            self.loans_taken += 1
            self.transaction_history.append((datetime.datetime.now(), 'Loan', amount))
            print(f"Loan of ${amount} granted. New balance: ${self.balance}")
    def transfer(self, amount, target_account_number, bank):
        if amount > self.balance:
            print("Insufficient funds for transfer")
        elif target_account_number not in bank.accounts:
            print("Account does not exist")
        else:
            self.balance -= amount
            bank.accounts[target_account_number].balance += amount
            self.transaction_history.append((datetime.datetime.now(), 'Transfer', amount))
            bank.accounts[target_account_number].transaction_history.append((datetime.datetime.now(), 'Received Transfer', amount))
            print(f"Transferred ${amount} to account {target_account_number}. New balance: ${self.balance}")
    def __str__(self):
        return f"Account({self.account_number}): {self.name}, {self.account_type}, Balance: ${self.balance}"




class Bank:
    next_account_number = 10000000  
    def __init__(self):
        self.total_balance = 0
        self.total_loan = 0
        self.loan_feature = True
        self.accounts = {}
    def create_account(self, name, email, address, account_type):
        account_number = Bank.next_account_number
        Bank.next_account_number += 1
        account = Account(name, email, address, account_type, account_number)
        self.accounts[account_number] = account
        print(f"Account created successfully! Account Number: {account_number}")
        return account_number
    def delete_account(self, account_number):
        if account_number in self.accounts:
            del self.accounts[account_number]
            print(f"Account {account_number} deleted successfully!")
        else:
            print("Account not found.")   
    def show_users(self):
        if self.accounts:
            for account in self.accounts.values():
                print(account)
        else:
            print("No accounts in the bank.")   
    def total_bank_balance(self):
        self.total_balance = sum(account.balance for account in self.accounts.values())
        print(f"Total available balance in the bank: ${self.total_balance}")    
    def total_bank_loan(self):
        print(f"Total loan amount given by the bank: ${self.total_loan}")  
    def off_loan(self):
        self.loan_feature = False
        print("Loan feature is now off.") 
    def on_loan(self):
        self.loan_feature = True
        print("Loan feature is now on.")


def user_menu(bank):
    while True:
        account_number = int(input("Enter your account number: "))
        if account_number in bank.accounts:
            customer = bank.accounts[account_number]
            break
        else:
            print("Invalid account number. Please try again.")

    while True:
        print(f"\nWelcome {customer.name}!!")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. View Transaction History")
        print("5. Take Loan")
        print("6. Transfer Money")
        print("7. Exit")
        
        choice = int(input("Enter Your Choice: "))
        if choice == 1:
            amount = float(input("Enter amount to deposit: "))
            customer.deposit(amount)
        elif choice == 2:
            amount = float(input("Enter amount to withdraw: "))
            customer.withdraw(amount)
        elif choice == 3:
            customer.check_balance()
        elif choice == 4:
            customer.view_transaction_history()
        elif choice == 5:
            amount = float(input("Enter loan amount: "))
            customer.take_loan(amount, bank)
        elif choice == 6:
            target_account_number = int(input("Enter target account number: "))
            amount = float(input("Enter amount to transfer: "))
            customer.transfer(amount, target_account_number, bank)
        elif choice == 7:
            break
        else:
            print("Invalid Input")

def admin_menu(bank):
    while True:
        print(f"\nWelcome Admin!!")
        print("1. Create Account")
        print("2. Delete Account")
        print("3. Show Users")
        print("4. Check Total Bank Balance")
        print("5. Check Total Loan Amount")
        print("6. Turn Off Loan Feature")
        print("7. Turn On Loan Feature")
        print("8. Exit")
        
        choice = int(input("Enter Your Choice: "))
        if choice == 1:
            name = input("Enter name: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            account_type = input("Enter account type (Savings/Current): ")
            bank.create_account(name, email, address, account_type)
        elif choice == 2:
            account_number = int(input("Enter account number to delete: "))
            bank.delete_account(account_number)
        elif choice == 3:
            bank.show_users()
        elif choice == 4:
            bank.total_bank_balance()
        elif choice == 5:
            bank.total_bank_loan()
        elif choice == 6:
            bank.off_loan()
        elif choice == 7:
            bank.on_loan()
        elif choice == 8:
            break
        else:
            print("Invalid Input")

def main_menu():
    bank = Bank()
    while True:
        print("\nWelcome!!")
        print("1. Customer")
        print("2. Admin")
        print("3. Exit")
        
        choice = int(input("Enter your choice: "))
        if choice == 1:
            user_menu(bank)
        elif choice == 2:
            admin_menu(bank)
        elif choice == 3:
            break
        else:
            print("Invalid Input")
bank = Bank()
while True:
        print("\nWelcome!!")
        print("1. Customer")
        print("2. Admin")
        print("3. Exit")
        
        choice = int(input("Enter your choice: "))
        if choice == 1:
            user_menu(bank)
        elif choice == 2:
            admin_menu(bank)
        elif choice == 3:
            break
        else:
            print("Invalid Input")