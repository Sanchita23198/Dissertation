import matplotlib
#matplotlib.use('TKAgg')
#import pandas as pd
#from pandas import Series, DataFrame
from matplotlib import animation
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
#import seaborn as sns
#matplotlib qt
import numpy as np
import time
import math

#from random import randrange
from random import randrange
#def animated_barplot():
N = 99

NR = int (N/3)
NP = int (N/3)
NS = int (N/3)

class Agent:
  def __init__(self, kind):
    self.kind = kind

P = []
P = [Agent("") for i in range (N)]

for i in range (N): # P = RPSRPSRPS
  A = Agent("")     #     012345678
  if (i % 3 == 0):
    A.kind="R"
  elif (i % 3 == 1):
    A.kind="P"
  else:
    A.kind="S"
  P[i]= A

x = []
x = ["" for i in range (3)]
x[0]="R"
x[1]="P"
x[2]="S"

y = [NR,NP,NS]
ax = plt.bar(x,y,0.5,0,align='center',color='green')

plt.draw()
plt.pause(0.01)

round = 1

while (NR+NP != 0 and NS+NP != 0 and NR+NS != 0):
  # identify Initiator
  Irand = randrange(0, N)

  # identify Responder 
  Rrand = randrange(0, N)

  C=P[Irand].kind+P[Rrand].kind

  if (C=="RP" or C=="PR"):
    P[Irand].kind="P"
    P[Rrand].kind="P"
    NR-=1
    NP+=1
  elif (C=="PS" or C=="SP"):
    P[Irand].kind="S"
    P[Rrand].kind="S"
    NP=NP-1
    NS=NS+1
  elif (C=="SR" or C=="RS"):
    P[Irand].kind="R"
    P[Rrand].kind="R"
    NS=NS-1
    NR=NR+1

   
  if (round % 1 == 0):
    ax.remove()
    y = [NR,NP,NS]
    ax = plt.bar(x,y,0.5,0,align='center',color='green')
    
    plt.draw()
    plt.pause(0.01)
    print(NR, NP, NS)
  round+=1

print(round, NR, NP, NS)
