#Clock function

import sys                      #System library
import curses                   #UI Library
    
from datetime import datetime   #System time

def clock(hourFormat, secondsTrue, windowSize):
    #Make clock window in the middle of the screen
    ClockWin = curses.newwin(6, 8, round(windowSize[1]/2), round(windowSize[0]/2))
    ClockWin.keypad(True)
    ClockWin.box()
    ClockWin.addstr(0, 1, "Clock")
    ClockWin.refresh()
    ClockWin.timeout(1000)

    #Loop through time
    while True:
        time = None
        if (secondsTrue == False) and (hourFormat == 12):
            time = datetime.now().strftime("%I:%M")

        elif (secondsTrue == True) and (hourFormat == 12):
            time = datetime.now().strftime("%I:%M:%S")

        elif (secondsTrue == False) and (hourFormat == 24):
            time = datetime.now().strftime("%H:%M")

        elif (secondsTrue == True) and (hourFormat == 24):
            time = datetime.now().strftime("%H:%M:%S")

        #Check for esc key
        key = ClockWin.getch()
        if key == 27:
            curses.endwin()
            sys.exit(0)

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
y, x = stdscr.getmaxyx()
size = [x, y]
clock(24, 1, size)
curses.endwin()
