class Account:
    def __init__(self, acc_no, holder):
        self.acc_no = acc_no
        self.holder = holder

    def show_details(self):
        print("Account No:", self.acc_no)
        print("Holder:", self.holder)

class SavingsAccount(Account):
    def __init__(self, acc_no, holder, balance):
        super().__init__(acc_no, holder)
        self.balance = balance

    def show_details(self):
        super().show_details()
        print("Balance:", self.balance)

sa = SavingsAccount("12345", "Riya", 5000)
sa.show_details()
