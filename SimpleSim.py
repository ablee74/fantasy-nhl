#Simple Simulator

import random
from Markov import *

#initiating Markov Stages

faceoff = markovStage('Faceoff')
T1 = markovStage('Team 1 has puck')
T2 = markovStage('Team 2 has puck')
t1Score = markovStage('Team 1 has scored a goal')
t2Score = markovStage('Team 2 has scored a goal')

#calls random.uniform - creates random probability for where puck will go

def faceoffGen():
    return random.uniform(0,1)

def scoreGen1():
    return random.uniform(0,300)

def scoreGen2():
    return random.uniform(0,300)

def resetFaceoff():
    return 0

def t1Turnover():
    return random.uniform(0,120)

def t2Turnover():
    return random.uniform(0,120)

#going to add connections between Markov stages

faceoff.addDest(T1, faceoffGen)
faceoff.addDest(T2, faceoffGen)
T1.addDest(t1Score, scoreGen1)
T2.addDest(t2Score, scoreGen2)
t1Score.addDest(faceoff, resetFaceoff)
t2Score.addDest(faceoff, resetFaceoff)
T1.addDest(T2, t1Turnover)
T2.addDest(T1, t2Turnover)

t1Goals = 0
t2Goals = 0

for x in range(3):
    timer = float(1200)
    currentStage = faceoff
    while timer > 0:
        print currentStage
        timeL = []
        for i in range(len(currentStage.densityL)):
            timeL.append( currentStage.densityL[i]() )
        duration = min(timeL)
        i = timeL.index(duration)
        currentStage = currentStage.destL[i]
        timer = timer - duration
        if currentStage == t1Score:
            t1Goals = t1Goals + 1
        elif currentStage == t2Score:
            t2Goals = t2Goals + 1
    print 'period', x+1, 'has ended'
        
