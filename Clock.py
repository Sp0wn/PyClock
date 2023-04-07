#Clock function

import curses

def clock(hourFormat, secondsTrue, windowSize):
    #Make clock window in the middle of the screen
    ClockWin = curses.newwin(6, 8, round(windowSize[1]/2), round(windowSize[0]/2))
    ClockWin.keypad(True)
    ClockWin.box()
    ClockWin.addstr(0, 1, "Clock")
    ClockWin.refresh()
    ClockWin.getch()

    #Loop through time
    while True:
        if (secondsTrue == False) and (hourFormat == 12):
            pass

        elif (secondsTrue == True) and (hourFormat == 12):
            pass

        elif (secondsTrue == False) and (hourFormat == 24):
            pass

        elif (secondsTrue == True) and (hourFormat == 24):
            pass

stdscr = curses.initscr()
y, x = stdscr.getmaxyx()
size = [x, y]
clock(1, 1, size)
curses.endwin()
