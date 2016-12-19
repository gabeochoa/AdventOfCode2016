import sys
import math
import re
import time
from collections import defaultdict

stuffs = []
for line in sys.stdin:
    stuffs.append(line.strip())

registers = defaultdict(int)

def proc_loop(output, i, cmd):
    global registers
    if cmd[0] == "cpy":
        output.append("L"+str(i)+": "+cmd[2] + " = " + cmd[1] + ";")
        pass
    elif cmd[0] == "inc":
        output.append("L"+str(i)+": ++"+cmd[1] + ";")
    elif cmd[0] == "dec":
        output.append("L"+str(i)+": --"+cmd[1] + ";")
    elif cmd[0] == "jnz":
        x = i + int(cmd[2])
        output.append("L"+str(i)+": if(" + cmd[1] + " != 0) goto L"+str(x)+";")
    return cmd

def part(two = None):
    output = ["#include<stdio.h>", "int main(){"]
    alpha = "abcd"
    output += [' '.join(["int "+alpha[i]+"=0;" for i in range(len(alpha))])]
    if two:
        output.append("c = 1;")

    for i, line in enumerate(stuffs):
        #print i+1, line
        cmdspl = line.split()
        cmd = cmdspl[0]
        param1 = cmdspl[1]
        if cmd == "cpy" or cmd == "jnz":
            param2 = cmdspl[2]
            proc_loop(output, i, (cmd, param1, param2))
        else:
            proc_loop(output, i, (cmd, param1))
    output.append("L"+ str(i+1) + ": printf(\"%d\", a);")
    output.append("return 0;")
    output.append("}")
    for line in output:
        print line

part(two="stuff")