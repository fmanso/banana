from unityagents import UnityEnvironment
from dqn_agent import Agent
import torch

env = UnityEnvironment(file_name = "./Banana_Windows_x86_64/Banana.exe")

brain_name = env.brain_names[0]

agent = Agent(state_size=37, action_size=4, seed=0)
agent.qnetwork_local.load_state_dict(torch.load("checkpoint.pth"))
env_info = env.reset(train_mode=False)[brain_name]

while True:
    action = agent.act(env_info.vector_observations[0], 0.0)
    env_info = env.step(action.astype(int))[brain_name]