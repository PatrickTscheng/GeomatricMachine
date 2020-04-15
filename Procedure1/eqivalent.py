

class equivalent:

    def __init__(self, P1, R1, P2, R2, h):
        self.A2 = [[0 for i in range(4*(h+1))] for j in range(4*(h+1))]
        # according to equation (15) to calculate A2
        for j in range(4*(h+1)):
            for i in range(4*(h+1)):
                self.A2[i][j] = 