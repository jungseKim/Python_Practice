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

class Qplayer:
    def __init__(self, symbol,gama=0.9,sotf=0.7):
        self.symbol = symbol
        self.count = 0
        self.gama=gama
        self.soft=sotf
        self.states=[]
        self.states_value={}
        self.exp_rate=0.15

    def update(self,postion):
        self.states.append(postion)
        
    def rewardUpdate(self,reward):
        for s in reversed(self.states):
            if self.states_value.get(s) is None:
                self.states_value[s]=0
            self.states_value[s]=(1-self.soft)*self.states_value[s]\
                +self.soft*(self.gama*reward)
            reward=self.states_value[s]
        self.states=[]

    def randomChoice(self,positions):
        idx = np.random.choice(len(positions))
        return positions[idx]

    def chooseAction(self, positions, current_board):
        if np.random.uniform(0, 1) <= self.exp_rate:
            return self.randomChoice(positions)
        else:
            value_max = -1
            for p in positions:
                next_board = current_board.copy()
                next_board[p] = self.symbol
                next_boardHash = str(current_board.reshape(9))
                value = 0 if self.states_value.get(
                    next_boardHash) is None else self.states_value.get(next_boardHash)
                # print("value", value)
                if value >= value_max:
                    value_max = value
                    action = p
            if value==0:
                self.randomChoice(positions)
            return action

if __name__ == "__main__":
    p1 = Qplayer(1)
    p2 = Player(-1)
    border = Border()

    for x in range(2000):

        while border.done == False:
            if len(border.availablePositions()) == 0:
                p1.rewardUpdate(0.2)
                break
            position = border.availablePositions()
            if(border.symbol == 1):
                action = p1.chooseAction(position,border.state)
                position=border.step(action, 1)
                p1.update(position)
            else:
                action = p2.action(position)
                border.step(action, -1)
            if(border.done):
                if border.symbol == 1:
                    p1.rewardUpdate(1)
                    p1.count+=1
                #       reward 주고 player 계산
                else:
                    p1.rewardUpdate(-1)
                    p2.count += 1
        border.reset()

    print(p1.count/2000)
