from pickle import STOP
import numpy as np



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
                    positions.append((i, j))  
        return positions

    def getHash(self):
        return str(self.state.reshape(self.row * self.col))

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

        return self.getHash()


class Player:
    def __init__(self, symbol):
        self.symbol = symbol
        self.count = 0

    def action(self, positions):
        idx = np.random.choice(len(positions))
        return positions[idx]


class Qplayer:
    def __init__(self, symbol, gama=0.9, sotf=0.7):
        self.symbol = symbol
        self.count = 0
        self.gama = gama
        self.soft = sotf
        self.states = []
        self.states_value = {}
        self.exp_rate = 0.15

    def update(self, postion):
        self.states.append(postion)

    def rewardUpdate(self, reward):
        for s in reversed(self.states):
            if self.states_value.get(s) is None:
                self.states_value[s] = 0
            self.states_value[s] += self.soft * \
                (self.gama * reward - self.states_value[s])
            reward = self.states_value[s]
        self.states = []

    def randomChoice(self, positions):
        idx = np.random.choice(len(positions))
        action = positions[idx]
        # print(action)
        return action

    def chooseAction(self, positions, current_board):
        if np.random.uniform(0, 1) <= self.exp_rate:
            # print(np.random.uniform(0, 1),'zzz')
            return self.randomChoice(positions)
        else:
            value_max = -999
            for p in positions:
                next_board = current_board.copy()
                next_board[p] = self.symbol
                next_boardHash = str(next_board.reshape(9))
    
                value = 0 if self.states_value.get(
                    next_boardHash) is None else self.states_value.get(next_boardHash)
               
                if value >= value_max:
                    value_max = value
                    action = p

            return action


if __name__ == "__main__":
    p1 = Qplayer(1)
    p2 = Qplayer(-1)
    border = Border()

    musyoubu = 0
    for x in range(50000):

        while border.done == False:
            if len(border.availablePositions()) == 0:
                p1.rewardUpdate(0.2)
                p2.rewardUpdate(0.2)
                musyoubu += 1
                break
            position = border.availablePositions()
            if(border.symbol == 1):
                action = p1.chooseAction(position, border.state)
                position = border.step(action, 1)
                p1.update(position)
            else:
                action = p2.chooseAction(position, border.state)
                position = border.step(action, -1)
                p2.update(position)
            if(border.done):
                if border.symbol == 1:
                    p1.rewardUpdate(1)
                    p1.count += 1
                    p2.rewardUpdate(-1)
                else:
                    p1.rewardUpdate(-1)
                    p2.rewardUpdate(1)
                    p2.count += 1
        p2.exp_rate = (0.5-x/35000)
        p1.exp_rate = (0.5-x/35000)
        border.reset()
    print(musyoubu/10000, '무승부수')
    print('게이시작 아무 버튼 눌러주세요')
    while input() != 's':
        while border.done == False:
            print(border.state)
            if len(border.availablePositions()) == 0:
                print('비김')
                break

            position = border.availablePositions()
            if(border.symbol == 1):
                check = int(input("Input your action row:"))
                if(check < 4):
                    action = (0, check-1)
                elif(check < 7 and check > 3):
                    action = (1, check-4)
                else:
                    action = (2, check-7)
                border.step(action, 1)

            else:
                action = p2.chooseAction(position, border.state)
                position = border.step(action, -1)

            if(border.done):
                if border.symbol == 1:
                    print('니가이김')
                else:
                    print('기계가이김')
                print(border.state)
        print('끝내려면 s 눌러')
        border.reset()
