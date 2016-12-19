import sys
import math

stuff = []
for line in sys.stdin:
    stuff.append(line.strip())

def valid(sides):
    a, b,c = (sides)
    if a+b > c:
        return True
    return False

i = 0
for line in stuff:
    sides = sorted([int(a) for a in line.split()])
    if not valid(sides):
        pass
    else:
        i+=1
print i
i=0
stuff2 = [[int(a) for a in line.split()] for line in stuff]
print stuff2
j = 0
while j < len(stuff2)-2:
    print "-----" + str(j)
    for k in range(0, 3):
        #  print k
        #  print stuff2[j]
        #  print stuff2[j][k]
        #  print stuff2[j+1][k]
        #  print stuff2[j+2][k]
        sides = sorted([stuff2[j][k], stuff2[j+1][k], stuff2[j+2][k]])
        if not valid(sides):
            pass
        else:
            print "pass : " +str(sides)
            i+=1
    j+=2
print i
