
# __（アンダースコア2つ）から始まる変数や関数は、そのクラス内でしか参照できなくなります
# 初期化する時は他のクラスからの影響を受けては困りますので、そのような配慮がなされています
# 定義は手動（自分で明記する必要がある）、代入は自動です

class Human():
    
    def __init__(self, age=0, last_name="", first_name="", blood_type=""):
        self.age = age
        self.last_name = last_name
        self.first_name = first_name
        self.blood_type = blood_type
    
h1 = Human()
h2 = Human(age=33, last_name="Tanaka", first_name="Ichiro", blood_type="O")

print(h1.age, h1.last_name, h1.first_name, h1.blood_type)
print(h2.age, h2.last_name, h2.first_name, h2.blood_type)

# object自信が因数な時がある
# ローカル変数（関数内部で初期化される変数）とグローバル変数区別がつかなくなるから

class Sample:

    num = 100

    def get_my_self(self):
        return self
    
    def show_num(self):
        num = 200
        print(self.num)
        print(num)

a = Sample()
b = a.get_my_self()
print(a is b)

a.show_num()

