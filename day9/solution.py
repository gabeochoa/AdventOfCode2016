import sys
import math
import re
import time

stuffs = []
for line in sys.stdin:
    stuffs.append(line.strip())

#stuffs = ["(27x12)(20x12)(13x14)(7x10)(1x12)A"]
#print stuffs
def convert(aa):
    x, y = aa.split("x")
    return (int(x), int(y))

def part1(stuff):
    cur_text = ""
    cur_numA = "0"
    cur_numB = "0"
    while True:
        try:
            letter = stuff[0]
        except Exception, e:
            break
        stuff = stuff[1:]
        if re.match("[A-Z]", letter):
            cur_text += letter
        else:
            if letter == "(":
                a = stuff.find(")")
                x,y = convert(stuff[0:a])
                for i in range(y):
                    cur_text += stuff[a+1:a+x+1]
                stuff = stuff[a+x+1:]
    return len(cur_text)

def part2(stuff):
    if '(' not in stuff:
        return len(stuff)
    ret = 0
    while '(' in stuff:
        a = stuff.find("(")
        stuff = stuff[a:]
        b = stuff.find(")")
        ret += a
        x,y = convert(stuff[1:b])

        stuff = stuff[b+1:]
        ret += part2(stuff[:x]) * y
        stuff = stuff[x:]
    ret += len(stuff)
    return ret

print "PART1", part1(stuffs[0])
print "PART2", part2(stuffs[0])