# Project Navigation

## Project Details

The project aims to resolve the problem of an agent that moves in an environment while picking yellow bananas and avoiding blue bananas.

Collecting yellow bananas provides +1 reward, collecting blue bananas provides -1 reward.

The state space has 37 dimensions containing the agent's dinamic state (velocity, position, etc) and ray-based perception of objects around the agent's forward position.

The actions available are:
* 0 - move forward
* 1 - move backward
* 2 - turn left
* 3 - turn right

## Getting Started

The code uses Python 3.6 and to install the required dependencies follow these instructions:
1. Clone the [DRLND Github repository](https://github.com/udacity/deep-reinforcement-learning#dependencies) and follow the instructions on the README.md file to install Pytorch, the ML-Agents toolkit, and a few more Python packages.
2. Download the Unity Environment and unzip it in a convenient directory:
  * Linux: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Linux.zip)
  * Mac OSX: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana.app.zip)
  * Windows (32-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Windows_x86.zip)
  * Windows (64-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Windows_x86_64.zip)
3. At the beginning of the files **train.py** and **play.py** there is a path to the Unity Environment. You need to edit the path and points to where you unzipped it.  
## Instructions

To train the agent run the **train.py** file. Prior execution the path to the banana environment must be edited at the beginning of the file.

**train.py** will train the Q-Network and save the weights of the network to the '**checkpoint.pth**' file when the goal of 13 average reward is achieved.

In addition, the **play.py** script loads the **checkpoint.pth** weights into the network and play the environment. Don't forget to edit the path to the banana environment. 
