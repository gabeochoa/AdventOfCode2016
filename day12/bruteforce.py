import sys
import math
import re
import time
from collections import defaultdict

stuffs = []
for line in sys.stdin:
    stuffs.append(line.strip())

print stuffs
registers = defaultdict(int)

def cpy(qx,ry):
    global registers
    try:
        val = int(qx)
        registers[ry] = val
    except ValueError:
        registers[ry] = registers[qx]
    return 1

def inc(rx):
    global registers
    registers[rx]+=1
    return 1

def dec(rx):
    global registers
    registers[rx]-=1
    return 1

def jnz(rx, vy):
    return vy if registers[rx] != 0 else 1

def proc_loop(i, cmd):
    global registers
    if cmd[0] == "cpy":
        i += cpy(cmd[1], cmd[2])
    elif cmd[0] == "inc":
        i += inc(cmd[1])
    elif cmd[0] == "dec":
        i += dec(cmd[1])
    elif cmd[0] == "jnz":
        i += jnz(cmd[1], int(cmd[2]))
    return i

i = 0
import os
while i < len(stuffs):
    print i+1, stuffs[i]
    cmdspl = stuffs[i].split()
    cmd = cmdspl[0]
    param1 = cmdspl[1]
    param2 = None
    if cmd == "cpy" or cmd == "jnz":
        param2 = cmdspl[2]
        i = proc_loop(i, (cmd, param1, param2))
    else:
        i = proc_loop(i, (cmd, param1))

    print i+1, registers