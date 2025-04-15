

class BankAccount:
    
    # 
    # Accounts can easily have 0 balance when they are opened.
    #
    def __init__(self, acc_num, acc_holder_name, initial_balance=0.0) -> None:
        self.account_number: int = acc_num
        self.account_holder_name: str = acc_holder_name
        self.balance: float = 0.0
        if initial_balance > 0: #prevent initializing bank account with negative balance
            self.balance = initial_balance
    

    def deposit(self, amount):
        if amount <= 0: #prevent depositing non positive amounts.
            return False
        else:
            self.balance += amount
            return True
    
    def withdraw(self, amount):
        if amount <= 0: #Prevent withdrawing non positive amounts.
            return False
        if self.balance - amount < 0:
            return False
        else:
            self.balance -= amount
            return True
        

    def get_balance(self):
        return self.balance
    
    def get_account_info(self):
        return f"Account {self.account_number}, owned by {self.account_holder_name}.\nBalance: {self.balance}"
    

    
        
