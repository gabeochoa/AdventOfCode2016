import sys
import math

stuff = []
for line in sys.stdin:
    stuff.append(line.strip())

def kp(keypad, start):
    return keypad[start[1]][start[0]]

def mv(matrix, x, y, dx, dy):
    try:
        if x+dx < 0 or y+dy < 0:
            return [x,y]
        aa = matrix.__getitem__(x+dx)[y+dy]
        if aa == 0:
            return [x,y]
        return [x+dx, y+dy]
    except IndexError:
        return [x,y]

#first half
keypd = []
keypd.append([ 1, 2, 3])
keypd.append([ 4, 5, 6])
keypd.append([ 7, 8, 9])

start = [1, 1]
for line in stuff:
    dirs = list(line)
    for move in dirs:
        #  print start,
        if move == 'U':
            start = mv(keypd, start[0], start[1], 0, -1)
            #  start[1] = 0 if start[1] == 0 else start[1]-1
        elif move == 'D':
            start = mv(keypd, start[0], start[1], 0, +1)
            #  start[1] = 2 if start[1] == 2 else start[1]+1
        elif move == 'L':
            start = mv(keypd, start[0], start[1], -1, 0)
            #  start[0] = 0 if start[0] == 0 else start[0]-1
        elif move == 'R':
            start = mv(keypd, start[0], start[1], +1, 0)
            #  start[0] = 2 if start[0] == 2 else start[0]+1
        #  print move,
        #  print start,
        #  print " ",
        #  print kp(keypd, start)
    print kp(keypd, start),
    print "",
print ""

#second half
keypd = []
keypd.append([  0,  0,  1,  0,  0])
keypd.append([  0,  2,  3,  4,  0])
keypd.append([  5,  6,  7,  8,  9])
keypd.append([  0, 10, 11, 12,  0])
keypd.append([  0,  0, 13,  0,  0])

start = [0, 2]
for line in stuff:
    dirs = list(line)
    for move in dirs:
        if move == 'U':
            start = mv(keypd, start[0], start[1], 0, -1)
        elif move == 'D':
            start = mv(keypd, start[0], start[1], 0, +1)
        elif move == 'L':
            start = mv(keypd, start[0], start[1], -1, 0)
        elif move == 'R':
            start = mv(keypd, start[0], start[1], +1, 0)
    print keypd[start[1]][start[0]],
    print " ",
