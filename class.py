
# クラスを定義
class Human:
    age = 0
    last_name = ""
    first_name = ""
    blood_type = ""

# インスタンス化-山田哲人
h = Human()
h.age = 25
h.last_name = "Yamada"
h.first_name = "Tetsuto"
h.blood_type = "B"
print(h.age, h.last_name, h.first_name, h.blood_type)

# インスタンス化
office_lady = Human()
office_lady.age = 25

salaryman = Human()
salaryman.age = 35

senior = Human()
senior.age = 55

child = Human()
child.age = 10

print(office_lady.age)
print(salaryman.age)
print(senior.age)
print(child.age)

# object.method
s = "aaabb"
print(s.count("a"))
print(s.startswith("a"))
print(s.upper())
print(s.zfill(10))

# 

