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

l1 = tf.layers.dense(inputs=X, units=150, activation=tf.nn.relu)
l2 = tf.layers.dense(inputs=l1, units=120, activation=tf.nn.relu)
l3 = tf.layers.dense(inputs=l2, units=100, activation=tf.nn.relu)
l4 = tf.layers.dense(inputs=l3, units=100, activation=tf.nn.relu)
l5 = tf.layers.dense(inputs=l4, units=80, activation=tf.nn.relu)
l6 = tf.layers.dense(inputs=l5, units=80, activation=tf.nn.relu)

Qpred = tf.layers.dense(inputs=l6, units=9)

# Qpred = tf.matmul(X, W)


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
    for i in range(100000):

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

                border.step(action, -1)

                x1 = border.getHash()

                Qs1 = sess.run(Qpred, feed_dict={X: x1})

                position = border.availablePositions()
                tempQs = Qs1[:]

                for check2 in reversed(np.argsort(tempQs[0])):
                    if(check < 4):
                        action = (0, check2-1)
                    elif(check < 7 and check2 > 3):
                        action = (1, check2-4)
                    else:
                        action = (2, check2-7)
                    if action in position:
                        Qs[0, check] = 0.9*Qs1[0, check2]
                        break

                sess.run(train, feed_dict={X: x, Y: Qs})
                # Qs1 = sess.run(Qpred, feed_dict={X: border.getHash()})

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
    print(musyoubu/100000, '?????????')
    print('???????????? ?????? ?????? ???????????????')
    while input() != 's':
        while border.done == False:
            print(border.state)
            if len(border.availablePositions()) == 0:
                print('??????')
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

                    for check in reversed(np.argsort(tempQs[0])):
                        if(check < 4):
                            action = (0, check-1)
                        elif(check < 7 and check > 3):
                            action = (1, check-4)
                        else:
                            action = (2, check-7)
                        if action in position:
                            # print(action)
                            break

                border.step(action, -1)

            if(border.done):
                if border.symbol == 1:
                    print('????????????')
                else:
                    print('???????????????')
                print(border.state)
        print('???????????? s ??????')
        border.reset()
