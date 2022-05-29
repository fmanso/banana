# Project Navigation

## Project Details

The project aims to resolve the problem of an agent that moves in an environment while picking yellow bananas and avoiding blue bananas.

Collecting yellow bananas provides +1 reward, blue bananas provide -1 reward.

The state space has 37 dimensions containing the agent's dinamic state (velocity, position, etc) and ray-based perception of objects around the agent's forward position.

The actions available are:
* 0 - move forward
* 1 - move backward
* 2 - turn left
* 3 - turn right

## Getting Started


## Instructions

To train the agent use the train.py file. Prior execution the path to the banana environment must be edited at the beginning of the file.

train.py will train the Q-Network and save the weights of the network to the 'checkpoint.pth' file when the goal is achieved.

In addition, the play.py script loads the checkpoint.pth weights into the network and play the environment. Don't forget to edit the path to the banana environment. 