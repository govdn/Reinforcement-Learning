# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 19:00:11 2019

@author: goverdhan
"""


import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("darkgrid")
import random

def nextState(initState, action):
    if(initState[0] == 0 and initState[1] == 1 and action[0] == 0 and action[1] == -1):
        temp1 = random.random()
        if(temp1<=0.7): modState = [0,0]
        elif(0.7 < temp1 <= 0.8): modState =[1,1]
        elif(0.8 < temp1 <= 0.9): modState =[0,2]
        elif(0.9 < temp1 <= 1.0): modState =[0,1]
        return modState
    if((initState[0] == 1 and initState[1] == 1) and ((action[0] == 0 and action[1] == -1) or (action[0] == -1 and action[1] == 0))):
        temp2 = random.random()
        if(temp2 <= 0.4): modState = [0,1]
        elif(0.4 < temp2 <= 0.8): modState =[1,0]
        elif(0.8 < temp2 <= 0.9): modState =[2,1]
        elif(0.9 < temp2 <= 1.0): modState =[1,2]
        return modState
    if((initState[0] == 0 and initState[1] == 3) and ((action[0] == 0 and action[1] == -1) or (action[0] == 1 and action[1] == 0))):
        temp3 = random.random()
        if(temp3 <= 0.4): modState = [0,2]
        elif(0.4 < temp3 <= 0.8): modState =[1,3]
        elif(0.8 < temp3 <= 1.0): modState =[0,3]
        return modState
    modState = list(np.array(initState)+np.array(action)) 
    return modState
        

def generateEpisode(beginState):
    initState = beginState
    episode = []
    while True:
        if list(initState) in terminationStates:
            return episode
        action = random.choice(actions)
        finalState = np.array(nextState(initState,action))
       # finalState = np.array(initState)+np.array(action) #should be modified
        if -1 in list(finalState) or gridSize in list(finalState):
            finalState = np.array(initState)
        episode.append([list(initState), action, rewardSize, list(finalState)])
        initState = finalState
        print(initState)

#parameters
gamma = 0.95 # discounting rate
rewardSize = -1
gridSize = 4
terminationStates = [[0,0], [gridSize-1, gridSize-1]]
actions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
numIterations = 70

#initializiation
V = np.zeros((gridSize, gridSize))
returns = {(i, j):list() for i in range(gridSize) for j in range(gridSize)}
deltas = {(i, j):list() for i in range(gridSize) for j in range(gridSize)}
states = [[i, j] for i in range(gridSize) for j in range(gridSize)]

for time in range(5):
    for beginState in (states[1:-1]):
        episode = generateEpisode(list(beginState))
        G = 0
        #print(episode)
        for i, step in enumerate(episode[::-1]):
            G = gamma*G + step[2]
            if step[0] not in [x[0] for x in episode[::-1][len(episode)-i:]]:
                idx = (step[0][0], step[0][1])
                returns[idx].append(G)
                newValue = np.average(returns[idx])
                deltas[idx[0], idx[1]].append(np.abs(V[idx[0], idx[1]]-newValue))
                V[idx[0], idx[1]] = newValue
plt.figure(figsize=(20,10))
all_series = [list(x)[:50] for x in deltas.values()]
for series in all_series:
    plt.plot(series)

        