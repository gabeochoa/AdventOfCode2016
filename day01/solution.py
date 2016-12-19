import sys
import math

stuff = []
dirr = ['n', 'e', 's', 'w']
for line in sys.stdin:
    stuff.append(line.split(","))

data = stuff[0]
double = None
oldpos = []
pos = [0, 0]
facing = 0

for direct in data:
    direct = direct.strip()
    oldpos.append(list(pos))

    d = direct[0]
    n = int(direct[1:])

    if d == "R":
        facing = (facing + 1) % 4
    else:
        facing = (facing - 1) % 4

    for i in range(0, n):
        if facing == 0:
            pos[1] -= 1
        elif facing == 1:
            pos[0] += 1
        elif facing == 2:
            pos[1] += 1
        elif facing == 3:
            pos[0] -= 1
        if pos in oldpos and double is None:
            double = list(pos)
            print "first double visit : ",
            print math.fabs(pos[0]) + math.fabs(pos[1])
        oldpos.append(list(pos))
print "Distance: ",
print math.fabs(pos[0]) + math.fabs(pos[1])
