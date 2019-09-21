
class A:
    def __init__(self):
        self.name = "Class A"
    
class B(A):
    pass

b = B()
print(b.name)

# new(old) child(parents)

class A:
    def funcA(self):
        print("func A")

class B(A):
    def funcB(self):
        print("func B")

b = B()
b.funcA()
b.funcB()

# 関数のオーバーライドをやってみよう
# super関数は親クラスのメソッドを使える

class A:

    def hello(self):
        print("Class A says hello")

class B(A):

    def hello(self):
        super().hello()
        print("Class B says hello")

b = B()
b.hello()

