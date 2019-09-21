
# ポリモーフィズムとは、同名のメソッドが、インスタンスによって振る舞いを適切に変える
# 似ているけどふるまいの違うクラス
# 名前をアンダースコアで始めると、「名前を公開したくない」という意味になります
# アンダースコアで始まる変数にアクセスしていると、「何かおかしいことをしている」と注意を促す

class RoomCounter:

    def __init__(self):
        self._num_air = 0
        self._num_room = 0
    
    def room_in(self, num):
        self._num_air = num
        self._num_room += num
    
    def room_out(self):
        self._num_room -= 1

    def num_room(self):
        return self._num_room

rc = RoomCounter()
rc.room_in(3)
rc.room_out()
print(rc._num_air)
print(rc._num_room)



