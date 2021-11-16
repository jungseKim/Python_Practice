import numpy as np
import tensorflow as tf
import random

# import collections import deque


class DQN:
    def __init__(self, session, input_size, output_size, name="main"):
        self.session = session
        self.input_size = input_size
        self.output_size = output_size
        self.name = name

        self._build_network()

    # def _build_network():
    #     with tf.variable_scope(self.net_name)
