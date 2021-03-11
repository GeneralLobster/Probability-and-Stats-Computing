# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 14:57:27 2021

@author: llim8
"""
import numpy as np
import random
import matplotlib.pyplot as plt

def diceRoll():#simulates the dice roll
    summation=random.randint(1,6)+random.randint(1,6)#we are getting the sum of two dice rolls
    count=0#will count the amount of attempts to get a sum of 7
    while summation!=7:#will keep attempting to get 7
        summation=random.randint(1,6)+random.randint(1,6)
        count+=1#increment for failures
    count+=1#since we did the summation once, we add one more attempt
    return count

successes=[]
i=0
for i in range(0,100000):
    steps=diceRoll()
    successes.append(steps)#appends the attempts
#print(successes)

#makes the graph
b = range(1, 30)
sb = np.size(b)
h1, bin_edges = np.histogram(successes, bins=b)
b1 = bin_edges[0:sb - 1]
probability = h1 / 100000

plt.stem(b1, probability)
plt.title("Probability to get a sum of 7")
plt.xlabel("Attempts to get Sum of 7")
plt.ylabel("Probability")
plt.show()