from unityagents import UnityEnvironment
import numpy as np

env = UnityEnvironment(file_name="./Banana_Windows_x86_64/Banana.exe")

brain_name = env.brain_names[0]
brain = env.brains[brain_name]

print(brain_name)
print(brain)