class a:
    def method_a(self):
        print("parent class a")


class b(a):
    def mathod_b(self):
        print("child class b")


x = b()
x.method_a()
x.mathod_b()
