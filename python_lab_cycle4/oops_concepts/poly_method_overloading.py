# class a:
#     def find_sum(self,a,b):
#         print(a+b)
#     def find_sum(self,a,b,c):
#         print(a+b+c)
#
# obj=a(1,2,3)
"""in python mathod overloading is not supported
so we can achieve indirectly using dafault argument concept"""


class a:
    def find_sum(self, a, b, c=0, d=0):
        print(a + b + c + d)


obj = a()
obj.find_sum(1, 2)
obj.find_sum(1, 2, 3)
