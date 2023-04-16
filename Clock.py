#Clock function

import sys                          #System library
import curses                       #UI Library
    
from datetime import datetime       #System time
from ASCII import convert_numbers   #ASCII Art

def clock(hourFormat, secondsTrue, windowSize):
    #Make clock window in the middle of the screen
    ClockWin = curses.newwin(7, 66, round(windowSize[1]/2)-8, round(windowSize[0]/2)-32)
    ClockWin.keypad(True)
    ClockWin.timeout(1000)

    #Loop through time
    while True:
        #Resets time string
        time = None

        #Changes time format depending on arguments
        if (secondsTrue == False) and (hourFormat == 12):
            time = datetime.now().strftime("%I:%M")

        elif (secondsTrue == True) and (hourFormat == 12):
            time = datetime.now().strftime("%I:%M:%S")

        elif (secondsTrue == False) and (hourFormat == 24):
            time = datetime.now().strftime("%H:%M")

        elif (secondsTrue == True) and (hourFormat == 24):
            time = datetime.now().strftime("%H:%M:%S")

        #Creates window box
        ClockWin.attron(curses.color_pair(1))
        ClockWin.clear()
        ClockWin.box()
        ClockWin.addstr(0, 1, "Clock")
        ClockWin.attroff(curses.color_pair(1))
 
        #Sets coordinates variables
        x = 1
        y = 1

        #Creates offset to center clock
        if secondsTrue == False:
            x = x + 12

        #Get the ascii art array
        asciiNumbers = convert_numbers(time)
        #Loops through the array of arrays
        ClockWin.attron(curses.color_pair(2))
        for arr in asciiNumbers:
            for line in arr:
                ClockWin.addstr(y, x, line)
                y = y + 1
            x = x + 8
            y = 1

        ClockWin.attroff(curses.color_pair(2))
        ClockWin.refresh()

        #Check for esc key
        key = ClockWin.getch()
        if key == 27:
            curses.endwin()
            sys.exit(0)
