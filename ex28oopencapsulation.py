class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number
        self._balance = balance
        
    def deposit(self, amount):
        self._balance += amount
        print(f"Deposited {amount}, new balance is {self._balance}")
        
    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew {amount}, new balance is {self._balance}")
        else:
            print("Insufficient balance")
account = BankAccount("123456789", 1000)
account.deposit(500)
account.withdraw(200)
