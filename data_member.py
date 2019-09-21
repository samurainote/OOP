
print("\tI'm\tyours")

# class method
# cls means class itself
class TaxCalc:

    @classmethod
    def class_method(cls, price):
        assert cls.__name__ == TaxCalc.__name__
        return int(price * 0.08)

    @staticmethod
    def static_method(price):
        return int(price * 0.08)

print(TaxCalc.class_method(1000))
print(TaxCalc.static_method(1000))


# if __name__ == '__main__':

# publicとprivate
# クラス内部に閉じたアクセス
class Sample:

    num1 = 100
    __num2 = 200

    def __init__(self):
        self.__num3 = 300

    def show_num(self):
        print(Sample.__num2)
        print(self.__num3)

print(Sample.num1)

s = Sample()
s.show_num()

# アンダースコア2個で始まるクラス変数やインスタンス変数