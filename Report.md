# Learning Algorithm
The learning algorithm is based on the previous exercise that train the Lunar Lander. The code had to be adapter in order to handle the outputs of the new environment which have a different state space and actions. 

The nerual network used to resolve the problem two fully connected layers of 64 neurons with RELU activation followed by a fully connected layer of 4 neurons that maps the action space. 

A more complex neural netowrk with 3 more layers and doubling the units of each layer was tested but it provides no improvements and increased considerably the training time. 

# Rewards

The following picture depicts the rewards per episode as the Q-Network is trained. 

![Rewards per episode!](https://github.com/fmanso/banana/blob/main/learning_scores.png?raw=true)

To solve the environment a total of 509 episodes were needed. 

# Ideas for Future Work

To further improve this work extensions to Deep Q-Networks could be used:
* [Double DQN](https://arxiv.org/abs/1509.06461)
* [Prioritized experience replay](https://arxiv.org/abs/1511.05952)
* [Dueling DQN](https://arxiv.org/abs/1511.06581)
* [Rainbow](https://arxiv.org/abs/1710.02298)
