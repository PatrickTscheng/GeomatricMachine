class Probability:

    def __init__(self, A, B):
        self.A = A
        self.B = B
        self.total = 0
        self.percentage = 0

    def putin(self, a, b):
        if b == self.B:
            self.total += 1
            if a == self.A:
                self.percentage += 1

    def get(self):
        return self.percentage/self.total
