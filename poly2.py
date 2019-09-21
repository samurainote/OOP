
from poly import StatCount

class StatTime(StatCount):
    Time = 0

    def __init__(self):
        super().__init__()
        self._initime = StatTime.Time
        self._pretime = 0

    def assign(self, value):
        t = Te


