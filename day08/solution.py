import sys
import math
import re
import time

stuff = []
for line in sys.stdin:
    stuff.append(line.strip())

#stuff = stuff[:16]
class Screen(object):
    def __init__(self):
        self.screen = [[0 for y in range(0, 50)] for x in range(0, 6)]

    def draw_screen(self):
        print ""
        for x in range(len(self.screen)):
            for y in range(len(self.screen[x])):
                if self.screen[x][y] == 1:
                    print "X",
                else:
                    print " ",
            print ""
        return self

    def set_rect(self, rect):
        for i in range(0, min(len(self.screen), rect[1])):
            for j in range(0, min(len(self.screen[i]),rect[0])):
                self.screen[i][j] = 1
        return self

    def rot_row(self, row, rotnum):
        rotnum = rotnum % (len(self.screen[row]))
        self.screen[row] = self.screen[row][-rotnum:] + self.screen[row][:-rotnum]
        return self

    def rot_col(self, col, rotnum):
        rotnum = rotnum % (len(self.screen))
        col_to = []
        for y in range(len(self.screen)):
            col_to.append(self.screen[y][col])
        # print col_to
        col_to = col_to[-rotnum:] + col_to[:-rotnum]
        for y in range(len(self.screen)):
            self.screen[y][col] = col_to[y]
        return self

    def count_pix(self):
        c = 0
        for x in range(len(self.screen)):
            for y in range(len(self.screen[x])):
                if self.screen[x][y] == 1:
                    c += 1
        return c

scr = Screen()
scr.draw_screen()

for line in stuff:
    space = line.split()
    if space[0] == "rect":
        print line
        rect = [int(x) for x in space[1].split("x")]
        scr.set_rect(rect)
    elif space[0] == "rotate":
        if space[1] == "column":
            print "rotate col ",
            print space[2:]
            scr.rot_col(int(space[2].split('=')[1]), int(space[4]))
        else: #rot row
            print "rotate row ",
            print space[2:]
            scr.rot_row(int(space[2].split('=')[1]), int(space[4]))
    scr.draw_screen()
    #time.sleep(5)

print scr.count_pix()