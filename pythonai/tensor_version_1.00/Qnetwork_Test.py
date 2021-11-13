from tensorflow.python.ops.gen_array_ops import shape
# from pythonai.gym_Test.TicTacToeDemo import Border
# from pythonai.gym_Test.TicTacToeDemo import Player
import numpy as np
# from ..gym_Test.TicTacToeDemo import Border
import tensorflow as tf


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
        return np.reshape(self.state, [1, 9])
        #  return self.state.reshape(self.row * self.col)

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


X = tf.placeholder(tf.float32, [1, 9])
# print(X.shape)
W = tf.get_variable("W1", shape=[9, 9],
                    initializer=tf.contrib.layers.xavier_initializer())

Qpred = tf.matmul(X, W)


Y = tf.placeholder(shape=[1, 9], dtype=tf.float32)

loss = tf.reduce_sum(tf.square(Y-Qpred))

train = tf.train.AdamOptimizer(learning_rate=0.1).minimize(loss)

init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)


class Player:
    def __init__(self, symbol):
        self.symbol = symbol
        self.count = 0

    def action(self, positions):
        idx = np.random.choice(len(positions))
        return positions[idx]


border = Border()
if __name__ == "__main__":

    border = Border()
    p1 = Player(1)
    musyoubu = 0
    for i in range(5000):

        e = 1.0/((i/10)+1)
        while border.done == False:
            position = border.availablePositions()

            if len(border.availablePositions()) == 0:
                Qs[0:check] = 1
                sess.run(train, feed_dict={X: x, Y: Qs})
                break

            if(border.symbol == 1):
                action = p1.action(position)
                position = border.step(action, 1)

            else:
                x = border.getHash()

                Qs = sess.run(Qpred, feed_dict={X: x})

                if np.random.rand(1) < e:
                    check = np.random.choice(len(position))
                    action = position[check]
                else:
                    tempQs = Qs[:]
              #       np.sort(tempQs[0])
              #       print(tempQs)
                    for check in reversed(np.argsort(tempQs[0])):
                        print(check)
                        if(check < 4):
                            action = (0, check-1)
                        elif(check < 7 and check > 3):
                            action = (1, check-4)
                        else:
                            action = (2, check-7)
                        if action in position:
                            # print(action)
                            break
                print(action)
                border.step(action, -1)

              #   Qs1 = sess.run(Qpred, feed_dict={X: border.getHash()})

              #   Qs[0:check] = np.argmax(Qs1)
              #   sess.run(train, feed_dict={X: x, Y: Qs})

            if(border.done):
                if border.symbol == 1:
                    Qs[0:check] = -10
                    sess.run(train, feed_dict={X: x, Y: Qs})
                else:
                    musyoubu += 1
                    Qs[0:check] = 1
                    sess.run(train, feed_dict={X: x, Y: Qs})

        border.reset()
    print(musyoubu/5000, '승부수')
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
                x = border.getHash()

                Qs = sess.run(Qpred, feed_dict={X: x})

                if np.random.rand(1) < e:
                    check = np.random.choice(len(position))
                    action = position[check]
                else:
                    tempQs = Qs[:]
              #       np.sort(tempQs[0])
              #       print(tempQs)
                    for check in reversed(np.argsort(tempQs[0])):
                        print(check)
                        if(check < 4):
                            action = (0, check-1)
                        elif(check < 7 and check > 3):
                            action = (1, check-4)
                        else:
                            action = (2, check-7)
                        if action in position:
                            # print(action)
                            break

                print(action)
                border.step(action, -1)

            if(border.done):
                if border.symbol == 1:
                    print('니가이김')
                else:
                    print('기계가이김')
                print(border.state)
        print('끝내려면 s 눌러')
        border.reset()
