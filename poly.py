
class StatCount:
    def __init__(self):
        self._value = 0
        self._count = 0
        self._sum = 0

    def assign(self, value):
        self._value = value
        self._count += 1
        self._sum += value

    def value(self):
        return self._value

    def count(self):
        return self._count

    def mean(self):
        return self._sum / max(1, self._count)

def do_test():
    i = StatCount()
    i.assign(10)
    i.assign(20)
    print(i.value())
    print(i.count())
    print(i.mean())

# インポートされた際にプログラムが動かないようにする
if __name__ == "__main__":
    do_test()


