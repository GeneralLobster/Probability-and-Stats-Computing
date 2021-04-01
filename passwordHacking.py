# -*- coding: utf-8 -*-

import random
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o',
          'p','q','r','s','t','u','v','w','x','y','z']#creates a list of the alphabet
mypassword=""
i=0
for i in range(0,4):#generates the user password once, for runtime sake
    mypassword+=alphabet[random.randint(0,25)]#0-25 for the list so we get letters

def hackerCheck(mypassword,i,m):#completes the hacker attempt, taking in the password, k, and m
    j=0
    k=0
    for j in range(0,i*m):#will start the hacker password process
        hackerpassword=""
        for k in range(0,4):#generates the password in the hacker list, since I don't want to actually keep a list of 80k+
            hackerpassword+=alphabet[random.randint(0,25)]
        if mypassword==hackerpassword:#will check if the hackerpass is the same as mypassword
            return 1#if so, we return 1 as a success
    return 0#assuming we don't get a match in i*m attempts, return 0

success=0#counts the number of successes
j=0
k=1
"""
THIS IS FOR PART 1 OF 1.4
for j in range(0,1000):
    success+=hackerCheck(mypassword,k,80000)
print(success)
success=0"""
j=0
k=7
"""
THIS IS FOR PART 2 OF 1.4
for j in range(0,1000):
    success+=hackerCheck(mypassword,k,80000)
print(success)
success=0"""
k=7
j=0
"""THIS IS FOR PART 3 of 1.4"""
for j in range(0,1000):
    success+=hackerCheck(mypassword,k,48000)
print(success)
