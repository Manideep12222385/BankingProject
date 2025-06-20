class BankAccount:
    total_accounts=0
    def __init__(self, owner:str, balance:float=0.0):
        self.owner = owner
        self.__balance=balance
        BankAccount.total_accounts+=1

    @property
    def balance(self) -> float:
        return self.__balance

    @balance.setter
    def balance(self, value: float):
        if value >= 0:
            self.__balance = value
        else:
            print("Balance cannot be negative.")

    def deposit(self, amt:float):
        if amt>0:
            self.__balance+=amt
        else:
            print("Deposit amount cannot be negative.")

    def withdraw(self, amt:float):
        if amt<0:
            print("Amount should be positive.")
        elif amt > self.__balance:
            print("Insufficient Funds.")
        else:
            self.__balance-=amt

    def __str__(self):
        label = "owners" if " and " in self.owner else "owner"
        return f"BankAccount({label}={self.owner}, balance={self.__balance:.2f})"

    def __repr__(self):
        label = "owners" if " and " in self.owner else "owner"
        return f"(BankAccount({label}='{self.owner}', balance={self.__balance:.2f}))"

    def __add__(self, other):
        if isinstance(other, BankAccount):
            merged_owner = f"{self.owner} and {other.owner}"
            merged_balance = self.balance + other.balance
            merged = BankAccount(merged_owner, merged_balance)
            BankAccount.total_accounts -= 1  # Adjust count when merging
            return merged
        return NotImplemented

    def __del__(self):
        BankAccount.total_accounts -= 1

class SavingsAccount(BankAccount):
    def __init__(self, owner: str, balance: float = 0.0, interest_rate: float = 0.05):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest)

class CheckingAccount(BankAccount):
    def __init__(self, owner: str, balance: float = 0.0, overdraft_limit: float = 500.0):
        super().__init__(owner, balance)
        self._overdraft_limit = overdraft_limit

    def withdraw(self, amt: float):
        if amt < 0:
            print("Amount should be positive.")
        elif amt > self.balance + self._overdraft_limit:
            print("Overdraft limit exceeded.")
        else:
            self._BankAccount__balance -= amt

    @property
    def overdraft_limit(self):
        return self._overdraft_limit

    @overdraft_limit.setter
    def overdraft_limit(self, value: float):
        if value >= 0:
            self._overdraft_limit = value
        else:
            print("Overdraft limit must be non-negative.")

class Customer:
    def __init__(self, name: str):
        self._name = name
        self.accounts = []

    def add_account(self, account: BankAccount):
        if isinstance(account, BankAccount):
            self.accounts.append(account)
        else:
            print("Only BankAccount can be added.")

    def total_balance(self) -> float:
        return sum(account.balance for account in self.accounts)

    def transfer(self, from_acc, to_acc, amt):
        if from_acc in self.accounts and to_acc in self.accounts:
            from_acc.withdraw(amt)
            to_acc.deposit(amt)
            print(f"Transferred ₹{amt} from {from_acc.owner} to {to_acc.owner}")
        else:
            print("Transfer accounts not associated with this customer")

    def __str__(self):
        accs = '\n  '.join(str(acc) for acc in self.accounts)
        return f"Customer: {self._name}\n  Accounts:\n  {accs}\n  Total Balance: ₹{self.total_balance():.2f}"

def show_account_info(obj):
    try:
        balance = obj.balance if hasattr(obj, 'balance') else obj.get_balance()
        print(f"Owner: {obj.owner}, Balance: ₹{balance}")
    except AttributeError:
        print("Object does not support required attributes")

class Wallet:
    def __init__(self, owner, amount):
        self.owner = owner
        self.balance = amount