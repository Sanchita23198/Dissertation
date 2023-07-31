import matplotlib
matplotlib.use('TKAgg')
import matplotlib.pyplot as plt
import numpy as np
import time
import math

from random import randrange

N = 20000
DA = 5
DB = 10

NA = int (N/2)
NB = N - NA
NDA = 0
NDB = 0

class Agent:
  def __init__(self, kind, age):
    self.kind = kind
    self.age = age

P = []
P = [Agent("B",0) for i in range (N)]

for i in range (N):
  if (i % 2 == 0):
    P[i] = Agent("A",0)

sq = math.sqrt(N)

ax = plt.subplot()
ax.set_xlim((0, 8))
ax.set_ylim((0, 8))

Acircle = plt.Circle((2,4),0.1+2*NA/N, color = 'blue')
Bcircle = plt.Circle((6,4),0.1+2*NB/N, color = 'red')
DAcircle = plt.Circle((4,6),0.1+2*NDA/N, color = 'grey')
DBcircle = plt.Circle((4,2),0.1+2*NDB/N, color = 'grey')

ax.add_patch(Acircle)
ax.add_patch(Bcircle)
ax.add_patch(DAcircle)
ax.add_patch(DBcircle)
                          
plt.draw()
plt.pause(0.001)

round = 1

while (True):
  while True:
    # identify Initiator
    Irand = randrange(0, N)

    # identify Responder 
    Rrand = randrange(0, N)

    if (Irand != Rrand):
        break

  # A is the initiator
  if (P[Irand].kind == "A"):
    if (P[Rrand].kind == "dB"):
      P[Rrand].kind = "A"
      P[Rrand].age = 0
      NDB -= 1
      NA += 1
    elif (P[Rrand].kind == "B"):
      P[Rrand].kind = "A"
      P[Rrand].age = 0
      NB -= 1
      NA += 1
      
    if ((P[Irand].age +1) == DA):
      P[Irand].kind = "dA"
      NA -= 1
      NDA += 1
    else:
      P[Irand].age += 1

  # B is the initiator
  elif (P[Irand].kind == "B"):
    if (P[Rrand].kind == "dA"):
      P[Rrand].kind = "B"
      P[Rrand].age = 0
      NDA -= 1
      NB += 1
    if ((P[Irand].age +1) == DB):
      P[Irand].kind = "dB"
      NB -= 1
      NDB += 1
    else:
      P[Irand].age += 1

  FR = 10

  if (round % int(N/FR) == 0):

    ax.remove()

    ax = plt.subplot()
    ax.set_xlim((0, 8))
    ax.set_ylim((0, 8))

    Acircle = plt.Circle((2,4),0.1+2*NA/N, color = 'blue')
    Bcircle = plt.Circle((6,4),0.1+2*NB/N, color = 'red')
    DAcircle = plt.Circle((4,6),0.1+2*NDA/N, color = 'grey')
    DBcircle = plt.Circle((4,2),0.1+2*NDB/N, color = 'grey')


    ax.add_patch(Acircle)
    ax.add_patch(Bcircle)
    ax.add_patch(DAcircle)
    ax.add_patch(DBcircle)
                              
    plt.draw()
    plt.pause(0.001)
      
    print(NA,NDA,NB,NDB,"(",round,int(round/N),")")
  round+=1
