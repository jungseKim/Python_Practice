import gym
import numpy as np
from numpy.core.fromnumeric import shape
import tensorflow as tf
import matplotlib.pyplot as plt

evn = gym.make('CartPole-v0')
evn.reset()
random_episodes = 0
reward_sum = 0

while random_episodes < 10:
    evn.render()
    action = evn.action_space.sample()
    observation, reward, done, _ = evn.step(action)
    print(observation, reward, done)
    reward_sum += reward
    if done:
        random_episodes += 1
        print('your episodes', reward_sum)
        reward_sum = 0
        evn.reset()
