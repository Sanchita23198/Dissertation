import matplotlib
matplotlib.use('TKAgg')
import matplotlib.pyplot as plt
import numpy as np
import time
import math

from random import randrange

N = 400
NL = 10
MH = 12

class Agent:
  def __init__(self, kind, time):
    self.kind = kind
    self.time = time

P = []
P = [Agent("F",0) for i in range (N)]

for i in range (NL):
  P[i] = Agent("L",0)


H = []
H = [0 for i in range (MH)]
H[0]=N

CH = []
CH = [0 for i in range (NL)]

sq = int(math.sqrt(N))

ax = plt.subplot()
ax.set_xlim((-0.5, sq+1.5))
ax.set_ylim((-0.5, sq+1))

circles = []
circles = [plt.Circle((1,1),1, color = 'blue') for i in range (N)]

xcentre = sq/2+1/2
ycentre = sq/2

for i in range (MH):
  if (H[i] > 0):
    circles[i] = plt.Circle((xcentre+(sq/2-1)*math.sin(math.radians(i*30)),ycentre+(sq/2-1)*math.cos(math.radians(i*30))),0.1+3*math.sqrt(H[i]/(2*math.pi*N)), color = 'blue')
  else:
    circles[i] = plt.Circle((xcentre+(sq/2-1)*math.sin(math.radians(i*30)),ycentre+(sq/2-1)*math.cos(math.radians(i*30))),0.1, color = 'green')


for i in range (MH):
  ax.add_patch(circles[i])

cleader = []
cleader = [plt.Circle((1,1),1, color = 'red') for i in range (NL)]

for i in range(NL):
  cleader[i] = plt.Circle((xcentre+(sq/2-1)*math.sin(math.radians(P[i].time*30)),ycentre+(sq/2-1)*math.cos(math.radians(P[i].time*30))),0.1, color = 'red')

for i in range(NL):
  ax.add_patch(cleader[i])
                          
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

  #first the case when leader and follower on the same hour
  if (P[Irand].kind == "L" #and P[Rrand].kind=="F"
      and (P[Irand].time == P[Rrand].time)):
    H[P[Rrand].time]-=1
    P[Rrand].time= (P[Rrand].time+1) % MH
    H[P[Rrand].time]+=1

  #  
  elif (
          (
            (P[Irand].time - P[Rrand].time > 0) and (P[Irand].time - P[Rrand].time < int(MH/2))
          )
          or
          (
            (P[Irand].time - P[Rrand].time < 0) and (P[Rrand].time - P[Irand].time > int(MH/2))
          )
        ):
    H[P[Rrand].time]-=1
    P[Rrand].time=P[Irand].time
    H[P[Rrand].time]+=1
    if (P[Rrand].kind == "L"):
      LH = P[Rrand].time

  if (round % int(N/10) == 0):

    ax.remove()

    ax = plt.subplot()
    ax.set_xlim((-0.5, sq+1.5))
    ax.set_ylim((-0.5, sq+1))

    circles = []
    circles = [plt.Circle((1,1),1, color = 'blue') for i in range (N)]

    for i in range (MH):
      if (H[i] > 0):
        circles[i] = plt.Circle((xcentre+(sq/2-1)*math.sin(math.radians(i*30)),ycentre+(sq/2-1)*math.cos(math.radians(i*30))),0.1+3*math.sqrt(H[i]/(2*math.pi*N)), color = 'blue')
      else:
        circles[i] = plt.Circle((xcentre+(sq/2-1)*math.sin(math.radians(i*30)),ycentre+(sq/2-1)*math.cos(math.radians(i*30))),0.1, color = 'green')

    for i in range (MH):
      ax.add_patch(circles[i])

    cleader = []
    cleader = [plt.Circle((1,1),1, color = 'red') for i in range (NL)]

    for i in range(NL):
      cleader[i] = plt.Circle((xcentre+(sq/2-1)*math.sin(math.radians(P[i].time*30)),ycentre+(sq/2-1)*math.cos(math.radians(P[i].time*30))),0.1, color = 'red')

    for i in range(NL):
      ax.add_patch(cleader[i])
                              
    plt.draw()
    plt.pause(0.001)

    for i in range (NL):
      CH[i] = H[i]
      
    print(CH)
  round+=1

#print(round, NR, NP, NS)
