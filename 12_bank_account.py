import json
import uuid
from datetime import datetime


class BankAccount:
    def __init__(self, owner, balance):
        self.account_id = str(uuid.uuid4())
        self.owner = owner
        self.balance = balance
        self.history = []
        self.add_transaction(transaction_type="ACCOUNT CREATED", amount=balance)

    def add_transaction(self, transaction_type, amount):
        transaction = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "type": transaction_type,
            "amount": amount,
            "balance_after": self.balance,
        }
        self.history.append(transaction)

    def deposit(self, amount):
        if amount <= 0:
            return "Amount must be positive"
        self.balance += amount
        self.add_transaction(transaction_type="DEPOSIT", amount=amount)
        self.save_history()
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return f"Insufficient balance! Current balance: {self.balance}"
        self.balance -= amount
        self.add_transaction(transaction_type="WITHDRAWL", amount=amount)
        self.save_history()
        return self.balance

    def get_balance(self):
        return f"{self.owner}'s balance: {self.balance}"

    def save_history(self):
        account_data = {
            "account_id": self.account_id,
            "owner": self.owner,
            "balance": self.balance,
            "history": self.history,
        }

        filename = f"{self.account_id}_history.json"

        with open(filename, "w") as f:
            json.dump(account_data, f, indent=2)

        print(f"History saved to {filename}")

    def show_history(self):
        heading = f"\nTransaction History of {self.account_id}"
        print(heading)
        print("-" * len(heading))

        for txn in self.history:
            print(
                f"{txn['timestamp']} | {txn['type']} | {txn['amount']} | Balance: {txn['balance_after']}"
            )

    def __str__(self):
        return f"Bank Account(id={self.account_id}, owner={self.owner}, balance={self.balance})"


arpan_acc = BankAccount("Arpan", 1000)

arpan_acc.deposit(500)
arpan_acc.withdraw(200)
arpan_acc.deposit(100)

print(arpan_acc)

arpan_acc.show_history()

arpan_acc.save_history()
