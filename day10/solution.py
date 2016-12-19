import sys
import math
import re
import time

stuffs = []
for line in sys.stdin:
    stuffs.append(line.strip())


botrex = 'bot (\d+) gives low to (output|bot) (\d+) and high to (output|bot) (\d+)'
dirsmap = {}
def getbots():
    global bots
    return [b for b in bots if len(bots[b]) == 2]

bots = {}
output = {}

def insVal(k, v):
    global bots
    if k not in bots:
        bots[k] = []
    bots[k] = list(sorted(bots[k] + [v]))

for line in stuffs:
    #  print line
    words = line.split()
    if words[0] == "value":
        #  print words
        valnum = int(words[1])
        botnum = int(words[5])
        insVal(botnum, valnum)
    else:
        bn, oA, onA, oB, onB = re.match(botrex, line).groups()
        bn, onA, onB = map(int, (bn, onA, onB))
        dirsmap[bn] = (oA, onA, oB, onB)


while len(getbots()) > 0:
    bn = getbots()[0]
    (oA, onA, oB, onB) = dirsmap[bn]
    vx, vy = bots[bn]
    if vx == 17 and vy == 61:
        print "part a", bn
    if oA == "output":
        output[onA] = vx
    else:
        insVal(onA, vx)
    if oB == "output":
        output[onB] = vy
    else:
        insVal(onB, vy)
    bots[bn] = []

print output[0] * output[1] * output[2]
