### 📘 Banking System Project

A simple Python-based simulation of a banking system to demonstrate object-oriented programming concepts. This project covers creating and managing different types of bank accounts, merging accounts, customer transfers, and duck typing.

---

### 📁 Project Structure

```
banking-system/
├── banking.py     
├── demo.py        
└── README.md      
```

---

### 📌 Features Demonstrated

#### ✅ Day 4 OOP Concepts Covered:

| Concept           | Implementation Example                                                  |
| ----------------- | ----------------------------------------------------------------------- |
| Classes & Objects | `BankAccount`, `SavingsAccount`, `CurrentAccount`, `Customer`           |
| Inheritance       | `SavingsAccount` and `CurrentAccount` inherit `BankAccount`             |
| Method Overriding | `withdraw` method behavior differs in derived classes                   |
| Special Methods   | `__str__`, `__repr__`, `__add__` for account merging                    |
| Duck Typing       | `print_account_summary()` accepts any object with `owner` and `balance` |
| Encapsulation     | Private attributes like `__balance`                                     |

---

### 💡 Functional Highlights

* **Bank Account Management**

  * Deposit & withdrawal
  * Overdraft and interest calculations
  * Account merging using `+` operator

* **Customer Class**

  * Manages multiple accounts
  * Allows inter-account transfers
  * Displays total balance

* **Account Merging**

  * When two accounts are merged, the total account count is updated correctly (e.g., from 4 to 3 if two accounts are merged)

---

### 🛠 How to Run

1. Make sure Python 3.10+ is installed.
2. Run the demo:

   ```bash
   python demo.py
   ```

---

### ⚙️ Design Decisions

* **Class separation**: Kept all logic in `banking.py` to follow separation of concerns.
* **Accurate account count after merging**: Removed merged accounts from the global list to keep count consistent.
* **Operator Overloading**: Used `__add__` to merge accounts, showcasing clean OOP practices.

---

### 🚧 Challenges Faced

* Ensuring correct object count after merging accounts.
* Balancing readability with use of OOP principles like encapsulation and operator overloading.
* Avoiding name errors (`_owner` vs `owner`) during object merging.

---

