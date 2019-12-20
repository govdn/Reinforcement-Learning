"""
title: Simulation of n bandit
Date: Sep-10,2019
author: goverdhan.r

"""
import numpy as np
import random
import math
import matplotlib.pyplot as plt

numberOfIterations = 1000
numberOfBandit = 2000
numberOfArms = 10


class Bandit:
    """docstring for Bandit."""

    def __init__(self):
        self.noOfTimes = []
        self.expectedReward = []
        self.estimatedReward = []
        self.noOfTimesUCB = []
        self.expectedRewardUCB = []
        self.estimatedRewardUCB = []
        for armIndex in range(numberOfArms):
            self.noOfTimes.append(0)
            self.expectedReward.append(0)
            self.estimatedReward.append(0)
            self.noOfTimesUCB.append(0)
            self.expectedRewardUCB.append(0)
            self.estimatedRewardUCB.append(0)

    def chooseArmNbandit(self, ep):
        """
        Chooses an arm with maximum estimated reward with probablity
        0f 1-epsilon and any arm with probablity epsilon
        """
        armChooser = random.random()
        if armChooser < (1-ep):
            return self.estimatedReward.index(max(self.estimatedReward))
        else:
            return random.randrange(numberOfArms)

    def updateExpReward(self, arm_I):
        """
        This function will update expected reward of choosen arm.
        """
        self.noOfTimes[arm_I] += 1
        self.estimatedReward[arm_I] = (BoxMuller()+self.estimatedReward[arm_I])/self.noOfTimes[arm_I]

    def chooseArmNbanditUCB(self,ep,t):
        """
        Choose an arm based on the UCB
        """
        for all_arm in range(numberOfArms):
            print(math.sqrt(math.log(t)/self.noOfTimesUCB[all_arm]))
            temp[all_arm] = self.estimatedRewardUCB[all_arm] + (math.sqrt(math.log(t)/self.noOfTimesUCB[all_arm]))
        return temp.index(max(temp))

    def updateExpRewardUCB(self, arm_J):
        self.estimatedRewardUCB[arm_J] = ((BoxMuller()-self.estimatedRewardUCB[arm_J])/self.noOfTimesUCB[arm_J])+self.estimatedRewardUCB[arm_J]
        self.noOfTimesUCB[arm_J] += 1

class epsilon(object):
    """docstring for epsilon."""

    def __init__(self, arg):
        self.ep = arg
        self.avgReward =[]
        self.avgRewardUCB = []

def BoxMuller():
    """
    Reward function
    generates random variable with
    guassian distribution with mean  of 0 and variance of 1
    """
    """"
    r1 = random.random()
    r2 = random.random()
    a  = 2.0 * math.pi * r1
    v  = math.sqrt( -2.0*math.log(r2))
    return (v * math.cos(a))
    """
    return (np.random.normal(0,1))


def main_thread():
    for epsilonIndex in all_epsilons:
        for iteration in range(numberOfIterations):
            epsilonIndex.avgReward.append(0)
            epsilonIndex.avgRewardUCB.append(0)
        for currentBandit in all_bandits:
            for armIndex in range(numberOfArms):
                currentBandit.estimatedReward[armIndex] = 0
                currentBandit.noOfTimes[armIndex] = 0
                currentBandit.estimatedRewardUCB[armIndex] = 0
                currentBandit.noOfTimesUCB[armIndex] = 1
            for iteration in range(numberOfIterations):
                arm_Choosen = currentBandit.chooseArmNbandit(epsilonIndex.ep)
                currentBandit.updateExpReward(arm_Choosen)
                epsilonIndex.avgReward[iteration] += sum(currentBandit.estimatedReward)/len(currentBandit.estimatedReward)
                """
                arm_ChoosenUCB = currentBandit.chooseArmNbanditUCB(epsilonIndex.ep,iteration)
                currentBandit.updateExpRewardUCB(arm_ChoosenUCB)
                epsilonIndex.avgRewardUCB[iteration] += sum(currentBandit.estimatedRewardUCB)/len(currentBandit.estimatedRewardUCB)
                """
    plt.plot(all_epsilons[0].avgReward, label = 'epsilon = 0.1')
    plt.plot(all_epsilons[1].avgReward, label = 'epsilon = 0.01')
    plt.plot(all_epsilons[2].avgReward, label = 'epsilon = 0')
    plt.legend(loc='upper left')
    plt.show()




all_bandits = []
for banditIndex in range(numberOfBandit):
    all_bandits.append(Bandit())
all_epsilons = []
all_epsilons.append(epsilon(0.1))
all_epsilons.append(epsilon(0.01))
all_epsilons.append(epsilon(0))
main_thread()
