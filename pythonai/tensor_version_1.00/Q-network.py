import gym
import numpy as np
import tensorflow as tf
from tensorflow.python.ops.gen_array_ops import shape
env = gym.make('FrozenLake-v0')

input_size = env.observation_space.n
output_size = env.action_space.n
ler_late = 0.1

X = tf.placeholder(shape=[1, input_size], dtype=tf.float32)
W = tf.Variable(tf.random_uniform([input_size, output_size], 0, 0.01))

print(X)

Qpred = tf.matmul(X, W)
Y = tf.placeholder(shape=[1, output_size], dtype=tf.float32)

loss = tf.reduce_sum(tf.square(Y-Qpred))

train = tf.train.GradientDescentOptimizer(
    learning_rate=ler_late).minimize(loss)

dis = 0.99
episodes = 5000

rList = []


def one_hot(x):
    return np.identity(16)[x:x+1]


init = tf.global_variables_initializer()
with tf.Session() as sess:
    # init = tf.initialize_all_variables()
    sess.run(init)
    for i in range(1):

        s = env.reset()
        e = 1.0/((i/50)+10)
        rAll = 0
        done = False
        local_loss = []

        while not done:
            Qs = sess.run(Qpred, feed_dict={X: one_hot(s)})
            #  예측값   현재상태 16(스테이트) 4(액션)
            if np.random.rand(1) < e:
                a = env.action_space.sample()
            else:
                a = np.argmax(Qs)
            a = np.argmax(Qs)
            # print(Qs, a)
            s1, reward, done, _ = env.step(a)
            # print(s1, reward, done)
            if done:
                Qs[0, a] = reward
                # print(s1)
            else:
                Qs1 = sess.run(Qpred, feed_dict={X: one_hot(s1)})
                # 행동한 action 값만 업대이트
                Qs[0, a] = reward+dis*np.max(Qs1)

            sess.run(train, feed_dict={X: one_hot(s), Y: Qs})

            rAll += reward
            s = s1
        rList.append(rAll)

print(sum(rList)/episodes)
