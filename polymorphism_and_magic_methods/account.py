class Account:
    def __init__(self, owner, amount=0):
        self.owner = owner
        self.amount = amount
        self._transactions = []

    def __add__(self, other):
        account = Account(f'{self.owner}&{other.owner}', self.amount + other.amount)
        account._transactions = self._transactions + other._transactions
        return account

    def __str__(self):
        return f"{__class__.__name__} of {self.owner} with starting amount: {self.amount}"

    def __repr__(self):
        return f"{__class__.__name__}({self.owner}, {self.amount})"

    def __len__(self):
        return len(self._transactions)

    def __getitem__(self, index):
        return self._transactions[index]

    def __reversed__(self):
        return reversed(self._transactions)

    def __eq__(self, other):
        return self.balance == other.balance

    def __gt__(self, other):
        return self.balance > other.balance

    def __ge__(self, other):
        return self.balance >= other.balance

    def add_transaction(self, amount):
        if not isinstance(amount, int):
            raise ValueError('please use int for amount')
        self._transactions.append(amount)

    @property
    def balance(self):
        return self.amount + sum(self._transactions)

    @staticmethod
    def validate_transaction(account, amount_to_add):
        if account.amount + amount_to_add < 0:
            raise ValueError("sorry cannot go in debt!")
        account._transactions.append(amount_to_add)
        return f"New balance: {account.balance}"


acc = Account('bob', 10)
acc2 = Account('john')
print(acc)  # Account of bob with starting amount: 10
print(repr(acc))  # Account(bob, 10)
acc.add_transaction(20)
acc.add_transaction(-20)
acc.add_transaction(30)
print(acc.balance)  # 40
print(len(acc))  # 3
for transaction in acc:
    print(transaction)  # 20, -20, 30
print(acc[1])  # -20
print(list(reversed(acc)))  # [30, -20, 20]
acc2.add_transaction(10)
acc2.add_transaction(60)
print(acc > acc2)  # F
print(acc >= acc2)  # F
print(acc < acc2)  # T
print(acc <= acc2)  # T
print(acc == acc2)  # F
print(acc != acc2)  # T
acc3 = acc + acc2
print(acc3)  # Account of bob&john with starting amount: 10
print(acc3._transactions)  # [20, -20, 30, 10, 60]
