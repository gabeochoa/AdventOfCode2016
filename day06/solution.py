import sys
import math
from collections import Counter
import re

stuff = []
for line in sys.stdin:
    stuff.append([x for x in line.strip()])

# part one
transp = [[0 for x in range(0, 26)] for y in range(len(stuff[0]))]

for row in range(0, len(stuff)):
    for col in range(0, len(stuff[row])):
        transp[col][int(ord(stuff[row][col]) - ord('a'))] += 1
for col in transp:
    print chr(col.index(max(col)) + ord('a')),
#part 2
print ""
for row in range(0, len(stuff)):
    for col in range(0, len(stuff[row])):
        transp[col][int(ord(stuff[row][col]) - ord('a'))] += 1
for col in transp:
    print chr(col.index(min(i for i in col if i > 0)) + ord('a')),
