class Buffer:
 
    def __init__(self, Buffer_lim: int):
        self.Buffer_lim = Buffer_lim
        self.storage = 0

    def check_null(self) -> bool:
        if self.storage == 0:
            return True
        else: 
            return False

    def check_full(self) -> bool:
        if self.storage is self.Buffer_lim:
            return True
        else: 
            return False

    def add_one(self) -> bool:
        if self.storage + 1 > self.Buffer_lim:  # 异常处理先不写了
            return False
        else:
            self.storage += 1
            return True

    def take_one(self) -> bool:
        if self.storage == 0:
            return False
        else:
            self.storage -= 1
            return True

    def get_measure(self) -> int:
        return self.storage
