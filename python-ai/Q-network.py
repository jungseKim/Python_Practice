import gym
import numpy as np
import tensorflow as tf
from tensorflow.python.ops.gen_array_ops import shape
env = gym.make('FrozenLake-v1')

input_size = env.observation_space.n
output_size = env.action_space.n
ler_late = 0.1

X = tf.constant(0, shape=(1, input_size), dtype=tf.float32)
W = tf.Variable(tf.random.uniform([input_size, output_size], 0, 0.01))

print(X)

Qpred = tf.matmul(X, W)
Y = tf.constant(0, shape=(1, output_size), dtype=tf.float32)

loss = tf.reduce_sum(tf.square(Y-Qpred))

train = tf.train.GradientDescentOptimizer(
    learning_rate=ler_late).minimize(loss)

dis = 0.99
episodes = 10

rList = []


with tf.Session() as sess:
    init = tf.initialize_all_variables()
    sess.run(init)
    for i in range(episodes):

        s = env.reset()
        e = 1.0/((i/50)+10)
        rAll = 0
        done = False
        local_loss = []

        while not done:
            Qs = sess.run(Qpred, feed_dict={X: np.one_hot(s)})
            #  예측값   현재상태 16(스테이트) 4(액션)
            if np.random.rand(1) < e:
                a = env.action_space.sample()
            else:
                a = np.argmax(Qs)

            s1, reward, done, _ = env.step(a)
            if done:
                Qs[0:a] = reward
            else:
                Qs1 = sess.run(Qpred, feed_dict={X: np.one_hot(s1)})

                Qs[0, a] = reward+dis*np.max(Qs1)

            sess.run(train, feed_dict={X: np.one_hot(s), Y: Qs})

            rAll += reward
            s = s1
        rList.append(rAll)

print(sum(rList)/episodes)
