import tkinter as tk
from tkinter import messagebox, simpledialog

class BankAccount:
    def __init__(self, account_number, account_holder, initial_balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

class BankingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Banking App")

        # Dictionary to store accounts with account number as key
        self.accounts = {}

        # Create buttons
        self.create_account_button = tk.Button(root, text="Create Account", command=self.create_account)
        self.create_account_button.pack(pady=5)

        self.deposit_button = tk.Button(root, text="Deposit", command=self.deposit, state=tk.DISABLED)
        self.deposit_button.pack(pady=5)

        self.withdraw_button = tk.Button(root, text="Withdraw", command=self.withdraw, state=tk.DISABLED)
        self.withdraw_button.pack(pady=5)

        self.check_balance_button = tk.Button(root, text="Check Balance", command=self.check_balance, state=tk.DISABLED)
        self.check_balance_button.pack(pady=5)

    def create_account(self):
        account_holder = simpledialog.askstring("Create Account", "Enter account holder's name:")
        if account_holder is not None:
            account_number = simpledialog.askinteger("Create Account", "Enter account number:")
            if account_number is not None:
                initial_balance = simpledialog.askfloat("Create Account", "Enter initial balance:")
                if initial_balance is not None:
                    if account_number not in self.accounts:
                        self.accounts[account_number] = BankAccount(account_number, account_holder, initial_balance)
                        messagebox.showinfo("Account Created", "Your account has been created successfully!")
                        self.enable_buttons()
                        self.update_account_info_label()
                    else:
                        messagebox.showwarning("Account Exists", "Account number already exists. Please choose a different number.")

    def deposit(self):
        account_number = simpledialog.askinteger("Deposit", "Enter your account number:")
        if account_number is not None:
            account = self.accounts.get(account_number)
            if account:
                amount = simpledialog.askfloat("Deposit", "Enter deposit amount:")
                if amount is not None:
                    if account.deposit(amount):
                        self.update_account_info_label()
                    else:
                        messagebox.showwarning("Invalid Amount", "Please enter a valid deposit amount.")
            else:
                messagebox.showwarning("Account Not Found", "Account number not found.")

    def withdraw(self):
        account_number = simpledialog.askinteger("Withdraw", "Enter your account number:")
        if account_number is not None:
            account = self.accounts.get(account_number)
            if account:
                amount = simpledialog.askfloat("Withdraw", "Enter withdrawal amount:")
                if amount is not None:
                    if account.withdraw(amount):
                        self.update_account_info_label()
                    else:
                        messagebox.showwarning("Invalid Amount", "Insufficient funds or invalid withdrawal amount.")
            else:
                messagebox.showwarning("Account Not Found", "Account number not found.")

    def check_balance(self):
        account_number = simpledialog.askinteger("Check Balance", "Enter your account number:")
        if account_number is not None:
            account = self.accounts.get(account_number)
            if account:
                messagebox.showinfo("Account Balance", "Account Holder: {}\nBalance: ${}".format(account.account_holder, account.balance))
            else:
                messagebox.showwarning("Account Not Found", "Account number not found.")

    def update_account_info_label(self):
        account_number = simpledialog.askinteger("Update Account Info", "Enter your account number:")
        if account_number is not None:
            account = self.accounts.get(account_number)
            if account:
                self.account_info_label.config(text="Account Holder: {} | Balance: ${}".format(account.account_holder, account.balance))
            else:
                messagebox.showwarning("Account Not Found", "Account number not found.")

    def enable_buttons(self):
        self.deposit_button["state"] = tk.NORMAL
        self.withdraw_button["state"] = tk.NORMAL
        self.check_balance_button["state"] = tk.NORMAL


if __name__ == "__main__":
    root = tk.Tk()
    app = BankingApp(root)
    root.mainloop()
 