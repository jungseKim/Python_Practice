from pickle import STOP
import numpy as np

# print(np.zeros((3, 3)))


class Border:
    def __init__(self, row=3, col=3, symbol=1):
        self.row = row
        self.col = col
        self.state = np.zeros((row, col))
        self.done = False
        self.symbol = symbol

    def reset(self):
        self.state = np.zeros((self.row, self.col))
        self.done = False
        self.symbol = 1

    def availablePositions(self):
        positions = []
        for i in range(self.row):
            for j in range(self.col):
                if self.state[i, j] == 0:
                    positions.append((i, j))  # need to be tuple
        return positions

    def getHash(self):
        return str(self.state.reshape(self.row * self.col))
        # [0. 0. 0. 0. 0. 0. 1. 0. 0.]
       #  return self.boardHash

    def soyobuCheck(self, endResult):
        for i in range(self.row):
            if sum(self.state[i, :]) == endResult:
                self.done = True

        for i in range(self.col):
            if sum(self.state[:, i]) == endResult:
                self.done = True
        diag_sum1 = sum([self.state[i, i] for i in range(3)])
        diag_sum2 = sum([self.state[i, 3 - i - 1]
                        for i in range(3)])
        diag_sum = max(abs(diag_sum1), abs(diag_sum2))
        if(diag_sum == 3):
            self.done = True

    def step(self, action, symbol):
        self.state[action] = symbol
        endResult = symbol*3

        self.soyobuCheck(endResult)

        if(self.done == False):
            self.symbol = self.symbol*-1

        return self.getHash(),


class Player:
    def __init__(self, symbol):
        self.symbol = symbol
        self.count = 0

    def action(self, positions):
        idx = np.random.choice(len(positions))
        return positions[idx]


if __name__ == "__main__":
    p1 = Player(1)
    p2 = Player(-1)
    border = Border()

    for x in range(4):

        while border.done == False:
           #      print(len(border.availablePositions()))
            if len(border.availablePositions()) == 0:
                break
            position = border.availablePositions()
            if(border.symbol == 1):
                action = p1.action(position)
                border.step(action, 1)
                # //업대이트
            else:
                action = p2.action(position)
                border.step(action, -1)
            if(border.done):
                if border.symbol == 1:
                    p1.count += 1
                #       reward 주고 player 계산
                else:
                    p2.count += 1
        border.reset()

    print(p1.count, p2.count)
