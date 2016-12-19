import sys
import math
from collections import Counter
import re

stuff = []
for line in sys.stdin:
    stuff.append(line.split(","))

aa = "aaaaa-bbb-z-y-x-123[abxyz]"
stuff = [aa]
for data in stuff:
    spot = (len(data) - data[::-1].find("-"))
    #  roomname = data[:spot-1].replace("-", "")
    roomname = data[:spot-1]
    letters = (x for x in roomname if x != "-")
    c = Counter(letters)
    five = [g for g in c.most_common(5)]
    five = [let[0] for let in sorted(five, key=lambda x : x[0])]
    #  print data[data.find("["):]
    #  print "["+''.join(five)+"]"
    print data
    if data[data.find("["):] == "["+''.join(five)+"]":
        print re.search(".*([0-9]+).*", data).groups()
