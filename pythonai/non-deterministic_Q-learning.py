import gym
import numpy as np
from gym.envs.registration import register
import random as pr


def rgrmax(vector):
    m = np.amax(vector)
    indices = np.nonzero(vector == m)[0]
    return pr.choice(indices)


env = gym.make('FrozenLake-v1')
Q = np.zeros([env.observation_space.n, env.action_space.n])
num_episodes = 2000

rList = []
dis = 0.99
learning_late = 0.85

for i in range(num_episodes):
    state = env.reset()
    rAll = 0
    done = False
    e = 1./((i/100)+1)

    while not done:
        action = np.argmax(
            Q[state, :]+np.random.randn(1, env.action_space.n)/(i+1))

        new_state, reward, done, _ = env.step(action)

#         dis카운트 곱해줌 (감마값 멀면 멀수록 값이 작아짐)
        Q[state, action] = (1-learning_late)*Q[state, action] + \
            reward+learning_late*(dis*np.max(Q[new_state, :]))

        rAll += reward
        state = new_state

    rList.append(rAll)

print(str(sum(rList)/num_episodes))
print(Q)
