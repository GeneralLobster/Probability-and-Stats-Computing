# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import random
        
p=np.array([0.10,  0.15,  0.20,  0.05,  0.30, 0.10, 0.10])#input of unfair dice

def nSidedDie(p):#this was from the lab instructions, modified to 6 unfair dice
    N=10000#number of trials
    s=np.zeros((N,1))
    n=6#sides of the dice
    cs=np.cumsum(p)
    cp=np.append(0,cs)
    for j in range(0,N):
        r=random.random()
        for k in range(0,n):
               if r>cp[k] and r<=cp[k+1]:
                   d=k+1
        s[j]=d 
    
    #graph
    b = range(1, len(p) + 2)
    sb = np.size(b)
    h1, bin_edges = np.histogram(s, bins=b)
    b1 = bin_edges[0:sb - 1]
    probability = h1 / N

    plt.stem(b1, probability)
    plt.title("Probability for n-sided die")
    plt.xlabel("Side of dice")
    plt.ylabel("Probability")
    plt.show()
    return s

def dice():
    N=10000
    p=[0.2, 0.1, 0.15, 0.3, 0.2, 0.05]
    cs=np.cumsum(p)
    cp=np.append(0,cs)
    for x in range(0,10000):
        for i in range(0,1000):
            listdice=[]
            for j in range(0,3):
                r = random.random()
                for k in range(0,len(p)):
                    if r>cp[k] and r<=cp[k+1]:
                        d=k+1
                listdice.append(d)
            if listdice[0]==1 and listdice[1]==2 and listdice[2]==3:
                print("Here")
print(dice())
