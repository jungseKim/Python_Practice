# import tf_agents
from tf_agents.environments import suite_gym
from tf_agents.environments import tf_py_environment
from tf_agents.agents.dqn import dqn_agent
from tf_agents.networks import q_network
from tf_agents.utils import common
from tf_agents.policies import random_tf_policy
import tensorflow as tf

env_name = 'CartPole-v0'

# 훈련용 검증용 2가지 환경 셋팅
train_py_env = suite_gym.load(env_name)
eval_py_env = suite_gym.load(env_name)

# python -> tenseor 랩핑
train_env = tf_py_environment.TFPyEnvironment(train_py_env)
eval_env = tf_py_environment.TFPyEnvironment(eval_py_env)

# QNetWork 신경망
q_net = q_network.QNetwork(
    # 입력망
    train_env.observation_spec(),
    # 출력망
    train_env.action_spec(),
    # 뉴런 갯수
    fc_layer_params=(100,)
)

optimizer = tf.compat.v1.train.AdamOptimizer(learning_rate=1e-3)
train_step_counter = tf.Variable(0)

agent = dqn_agent.DqnAgent(
    train_env.time_step_spec(),
    train_env.action_spec(),
    #     여기에 네트워크 포함
    q_network=q_net,
    optimizer=optimizer,
    #     loas함수지정
    td_errors_loss_fn=common.element_wise_squared_loss,
    train_step_counter=train_step_counter)

# 에이전트 초기화
agent.initialize()

# 현재정책
eval_policy = agent.policy
# 대이터 수집정책
collect_policy = agent.collect_policy
# 랜덤
random_policy = random_tf_policy.RandomTFPolicy(train_env.time_step_spec(),
                                                train_env.action_spec())
