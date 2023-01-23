class A:
    def __init__(self,num):
        self.number=num
    def display(self):
        print("constructor from parent class is working",self.number)

class B(A):
    def __init__(self,num,num1):
        super().__init__(num)
        self.number1=num1

    def display1(self):

        print("constructor from child class is working",self.number1)

obj=B(20,30)
obj.display()
obj.display1()

