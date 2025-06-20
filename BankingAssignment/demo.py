from banking import SavingsAccount, CheckingAccount, BankAccount, Customer, Wallet, show_account_info

s1 = SavingsAccount("Akshay", 1000, 0.05)
s2 = SavingsAccount("Preetham", 2000, 0.03)
c1 = CheckingAccount("Pavan", 500, 1000)
c2 = CheckingAccount("Nandu", 700, 300)

accounts = [s1, s2, c1, c2]

for acc in accounts:
    acc.deposit(100)
    acc.withdraw(200)
    if isinstance(acc, SavingsAccount):
        acc.apply_interest()

for acc in accounts:
    print(acc)

merged = s1 + c1
print("Merged Account:", merged)
print("Total Accounts:", BankAccount.total_accounts)

print("\n--- Customer & Transfer Demo ---")
acc1 = BankAccount("Mani", 1000)
acc2 = BankAccount("Teja", 500)
cust = Customer("Mani")
cust.add_account(acc1)
cust.add_account(acc2)
cust.transfer(acc1, acc2, 100)
print(cust)

print("\n--- Duck Typing Demo ---")
wallet = Wallet("Ravi", 300)
show_account_info(s1)
show_account_info(wallet)
