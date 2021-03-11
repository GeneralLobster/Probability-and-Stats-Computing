# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 15:09:16 2021

@author: llim8
"""
import random

def coinToss():#simulates 100 coin tosses
    i=0
    heads=0#will count hte number of heads
    for i in range(0,100):
        toss=random.randint(0,1)
        if toss==0:#if the toss is 0, we will say it is a heads and count up
            heads+=1
    return heads

i=0
successes=0
for i in range(0,100000):
    prob=coinToss()
    if prob==50:#if we get exactly 50 heads/successful tosses, we add 1 to our total success
        successes+=1
print(successes/100000)
