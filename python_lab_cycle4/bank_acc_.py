class Bankaccount:
    def __init__(self, num, nam, typ, bal):
        self.acc_number = num
        self.name = nam
        self.acc_type = typ
        self.balance = bal

    def withdraw(self, c):
        self.withdr = c
        self.balance = self.balance - self.withdr

    def deposit(self, c):
        self.dep = c
        self.balance = self.balance + self.dep

    def display(self):
        print("Account_number : ", self.acc_number)
        print("Name : ", self.name)
        print("Acc_type : ", self.acc_type)
        print("balance : ", self.balance)


x = Bankaccount(1234567, "Elon Musk", "savings", 100000)
x.display()
c = int(input("enter amount"))

choice = int(input("1.withdraw\n2.deposit"))
if choice == 1:
    x.withdraw(c)
    print("\nwithdrawed",c)
elif choice == 2:
    x.deposit(c)
    print("\ndeposited",c)
else:
    print("invalid")
print("\n")
x.display()
