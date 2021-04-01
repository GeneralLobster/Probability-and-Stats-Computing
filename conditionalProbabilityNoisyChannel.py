# -*- coding: utf-8 -*-
import random as r

#parameters given
p0=0.6
e0=0.05
p1=0.4#this was 1-p0
e1=0.03
N=100000

def roll(valProb):#this will determine whether or not the probability of valProb fails/success
    num=r.random()#generates random float from 0 to 1
    if num<valProb:##if the random number is less than the probability, we consider it a success
        return 1
    return 0#if not, we consider it a fail

def part1():#this gets the fail rate of a 1 bit message being transmitted wrong
    failures=0#counts for times of failures
    for i in range(0,N):#for 100,000 times, we simulate a bit message being transmitted
        bitMessage=roll(p0)#we roll for p0, since the message is either 0 or 1
        if bitMessage==1:
            """if the value of bitMessage is 1, then that means that the message sent is actually 0,
            since we are checking if we are getting a success of p0, and not p1"""
            bitMessage=roll(1-e0)#we roll the chances that there is no error for the message
            if bitMessage==0:#if the roll fails, it means that there is an error in the message
                failures+=1#increment failures
        else:#if the bitmessage is 0(meaning that the message being sent is 1)
            bitMessage=roll(1-e1)#we roll the chances that there is no error for the message
            if bitMessage==0:#if the roll fails, that means there is an error in the message
                failures+=1#increment failures
    return failures#we send back the number of fails

def part2():#this gets the success rate when you submit a signal S=1, that R=S=1
    successes=0#counts number of successes
    for i in range(0,N):
        bitMessage=roll(1-e1)#we roll the chance that there is no error for the message
        """We do 1-e1 since the only way S!=R and S=1 is 1-e1. We are ONLY looking at when S=1,
        therefore when S=0, the condition already fails. Due to this, we can assume every message
        sent is S=1, and we are only checking if R=1 or R=0, which is 1-e1"""
        if bitMessage==1:#if we get a 1, that means that the R is 1, so no error in message
            successes+=1#increment success
    return successes

def part3():#this gets the success rate when you recieve a signal R=1, that the sent signal was S=1
    successes=0#counts number of successes
    for i in range(0,N):
        bitMessage=roll(1-e0)
        """The assumption is that R=1, which can only be done when S=1, and there is no error OR that S=0 and there
        is an error since we are getting the success rate when S=1, then we must conclude that the message transmitted
        was not an error of S, which is S=0 and the R=1
        So we would need to check if when S=0 fails first, and then check if S=1 and it is a success"""
        if bitMessage==1:#with the assumption that the R did not come from S=0, we can then check for S=1, if not then S=0 when R=1
            bitMessage=roll(1-e1)#roll to see if S=1 is transmitted properly
            if bitMessage==1:#if S=1 is transmitted correectly add to success
                successes+=1
                
    return successes

def part4():#does the majority rule
    failures=0#checks to failures
    for i in range(0,N):
        transList=[]#we have our list for 3 numbers being transmitted
        bitMessage=roll(p0)#roll for S=0 or S=1
        if bitMessage==1:#when S=0
            for j in range(0,3):#we perform transmission 3 times
                transList.append(roll(1-e0))#roll for error of S=0
            countError=transList.count(0)
            #count the times that there is a failure(in this case, we are seeing if it failed to transmit S=0 correctly)
            if countError>1:#if there are more than 1(meaning 2 or 3), then it failes
                failures+=1
        else:#when bitMessage is S=1
            for j in range(0,3):#transmission 3 times
                transList.append(roll(1-e1))#roll for error of S=1
            countError=transList.count(0)
            #count times that there is a failure of S=1 transmission
            if countError>1:#if there are more than 1 failings, then it fails
                failures+=1
    return failures

x=part1()
print("The answer for Part 1: Probability of erroneous transmission is \n",x/N,"\n")
y=part2()
print("The answer for Part 2: Conditional probability: P(R= 1 | S= 1) is \n",y/N,"\n")
z=part3()
print("The answer for Part 3: Conditional probability: P(S= 1 | R= 1) is \n",z/N,"\n")
a=part4()
print("The answer for Part 4: Enhanced transmission method is \n",a/N,"\n")
