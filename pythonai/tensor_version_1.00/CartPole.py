import gym
import numpy as np
import tensorflow as tf
from tensorflow.python.framework import dtypes
from tensorflow.python.ops.gen_array_ops import shape
from tensorflow.python.ops.init_ops import Initializer

# 문제점
# 네트 워트가 작음 변수 가 적음

env = gym.make('CartPole-v0')
s = env.reset()


input_size = env.observation_space.shape[0]
output_size = env.action_space.n
# print(env.observation_space.shape[0])
# print(env.action_space)
# 상태값 변수는 4개 인데 그변수마다 값에 차이가 좆되서 큐태이블로 하면 개좆됨
# 액션값은 2개밖에 없는거 같음 왼 오 그래서 W shape의 shape 이 4*2

X = tf.placeholder(tf.float32, [None, input_size])
W = tf.get_variable("W1", shape=[input_size, output_size],
                    initializer=tf.contrib.layers.xavier_initializer())

Qpred = tf.matmul(X, W)

Y = tf.placeholder(shape=[None, output_size], dtype=tf.float32)

loss = tf.reduce_sum(tf.square(Y-Qpred))

train = tf.train.AdamOptimizer(learning_rate=0.1).minimize(loss)

episodes = 2000
dis = 0.9
rList = []
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

for i in range(episodes):
    e = 1.0/(0.1)
    rAll = 0
    s = env.reset()
    done = False
    step_count = 0
    while not done:
        step_count += 1
        x = np.reshape(s, [1, 4])
        # 리쉐입 1차원 ->2차원
        Qs = sess.run(Qpred, feed_dict={X: x})

        if np.random.rand(1) < e:
            a = env.action_space.sample()
        else:
            a = np.argmax(Qs)
        s1, reward, done, _ = env.step(a)

        if done:
            # 원래는 reward주는게 맞지만 이거는 끝나면 지는거니까
            Qs[0:a] = -100
        else:
            x1 = np.reshape(s1, [1, 4])
            Qs1 = sess.run(Qpred, feed_dict={X: x1})
            Qs[0:a] = np.argmax(Qs1)
        #     어차피 2차원 배열 리턴 되서 리쉐입 안해도됨

        sess.run(train, feed_dict={X: x, Y: Qs})
        s = s1

    rList.append(step_count)
    print(i, '번째', step_count)

observation = env.reset()
step_count = 0
while True:
    step_count += 1
    env.render()
    x = np.reshape(observation, [1, 4])
    Qs = sess.run(Qpred, feed_dict={X: x})
    print(Qs)
    a = np.argmax(Qs)
    observation, v, c, _ = env.step(a)
    if c:
        print(step_count)
        break
