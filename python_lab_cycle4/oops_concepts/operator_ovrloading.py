#we can give different meaning to an operator

class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def __add__(self, p2):  #magical function
        print("add operator called")
        final_price=self.price+p2.price
        print("final price = ",final_price)
    def __sub__(self, p2):
        print("sub operator called")
        final_price=self.price-p2.price
        print("final price = ",final_price)

p1=Product("iphone",10000)
p2=Product("mac book",20000)
p1+p2   #it means Product.__add__(p1,p2)
p2-p1