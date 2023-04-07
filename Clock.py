#Clock function

import curses

def clock(hourFormat, secondsTrue, windowSize):
    pass

stdscr = curses.initscr()
y, x = stdscr.getmaxyx()
size = [x, y]
clock(1, 1, size)
