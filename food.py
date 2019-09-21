
class Food:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def describe(self):
        print(self.name + "は" + str(self.price) + "円です")
    
    def discount(self, rate):
        t = self.price * ((100 - rate) / 100)
        return int(t)

f1 = Food("ラーメン", 800)
f1.describe()
print(f1.discount(20))

# def print 返すだけ, def return 変数





