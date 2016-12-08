import sys
import math
from collections import Counter
import re

stuff = []
for line in sys.stdin:
    stuff.append([x for x in line.strip()])

def ispal(s):
    for x in range(0, len(s)-3):
        if left_check(list(s[x:x+4])):
            #  print s[x:x+4]
            return list(s[x:x+4])
    return []

def left_check(lft):
    if lft[0] == lft[1]:
        return False
    if lft[0:2] != lft[3:1:-1]:
        return False
    return True

def ispal3(s):
    out = []
    for x in range(0, len(s)-2):
        if left_check3(list(s[x:x+3])):
            #  print s[x:x+3]
            out.append(list(s[x:x+3]))
    return out

def left_check3(lft):
    if lft[0] == lft[1]:
        return False
    if lft[0] != lft[2]:
        return False
    return True

def isIP(line):
    line = ''.join(line)
    bracket = re.compile(r'\[([a-z]+)\]')
    brackets = bracket.findall(line)
    palstr = str(line)
    for r in brackets:
        palstr = palstr.replace('['+r+']', ' ')
    issue = False
    for g in palstr.split(" "):
        if ispal(g):
            issue = True
    if not issue:
        return False
    # now check in brackets
    for r in brackets:
        if ispal(r):
            return False
    return True

def isIP2(line):
    line = ''.join(line)
    bracket = re.compile(r'\[([a-z]+)\]')
    brackets = bracket.findall(line)
    palstr = str(line)
    for r in brackets:
        palstr = palstr.replace('['+r+']', ' ')
    pals = []
    for g in palstr.split(" "):
        aaa = ispal3(g)
        if aaa != []:
            for aba in aaa:
                pals.append(aba)
    # now check in brackets
    print pals
    for r in brackets:
        for pal in pals:
            mypal = pal[1] + pal[0] + pal[1]
            if mypal in r:
                return True
    return False

count = 0
count2 = 0
for index, line in enumerate(stuff):
    if isIP(line):
        count+=1
    if isIP2(line):
        count2+=1

print count
print count2

