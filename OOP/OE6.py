class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("The amount should be non negative")
        
    def withdraw(self, amount):
        
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            return amount
        else:
            print("The amount should be non negative and not less than the balance")
            
    def display_account_info(self):
        return f"Account number: {self.__account_number}\nCurrent balance: {self.__balance}"
    
    def __display_balance(self):
        return self.__balance
    
    def get_account_number(self):
        return self.__account_number
    
    def get_balance(self):
        return display_balance()
    
    def set_account_number(self):
        return self.__account_number
    
    def set_balance(self, balance):
        if balance > 0:
            self.__balance = balance
        else:
            print("The balance should be non negative number")
            
account1 = BankAccount(1234, 0)

account1.deposit(1000.00)
account1.withdraw(500.00)
account1.set_balance(-600)
account1.display_account_info()
