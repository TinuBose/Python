# it is related to both inheritance and polymorphaism
class A:
    def function1(self):
        print("function one working")

    def func(self):
        print("function two working from class A")


class B(A):
    def function3(self):
        print("function three working")

    def func(self):
        super().func()   #used to take function from parent class
        print("function four working from class B ")


obj = B()
obj.func()  # same function name with no arguments in both parent and child class
# when func function of parent class will be overrided by func function of child class
# so func function of child class only work
# func method of parent become hidden
