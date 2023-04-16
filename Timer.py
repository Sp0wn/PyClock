#Timer function

import sys                          #System library
import curses                       #UI Library

from datetime import timedelta      #Time diff
from ASCII import convert_numbers   #ASCII Art

def timer(timeUnits, timeValues, windowSize):
    #Make timer window in the middle of the screen
    TimerWin = curses.newwin(7, 66, round(windowSize[1]/2)-8, round(windowSize[0]/2)-32)
    TimerWin.keypad(True)
    TimerWin.timeout(1000)

    #Sets time variables
    index = 0
    seconds = 0
    minutes = 0
    hours = 0

    #Loop through the list and assign numbers
    for t_unit in timeUnits:
        if t_unit == "s":
            seconds = timeValues[index]

        elif t_unit == "m":
            minutes = timeValues[index]

        elif t_unit == "h":
            hours = timeValues[index]
        
        index = index + 1

    #Adds the time values and get the time value in seconds
    time = timedelta(seconds=seconds, minutes=minutes, hours=hours)
    time_left = int(time.total_seconds())

    #Loops through the timer
    while time_left >= 0:
        #Creates window box
        TimerWin.attron(curses.color_pair(1))
        TimerWin.clear()
        TimerWin.box()
        TimerWin.addstr(0, 1, "Timer")
        TimerWin.attroff(curses.color_pair(1))
   
        #Adds zero at the start of the string
        time = str(time)
        if len(time) < 8:
            time = "0" + time

        #Sets coordinates variables
        x = 1
        y = 1

        #Get the ascii art array
        asciiNumbers = convert_numbers(time)
        #Loop through the array of arrays
        TimerWin.attron(curses.color_pair(2))
        for arr in asciiNumbers:
            for line in arr:
                TimerWin.addstr(y, x, line)
                y = y + 1
            x = x + 8
            y = 1

        #Decreases time by one second
        time_left = time_left - 1
        time = timedelta(seconds=time_left)

        TimerWin.attroff(curses.color_pair(2))
        TimerWin.refresh()
    
        #Checks for esc key
        key = TimerWin.getch()
        if key == 27:
            curses.endwin()
            sys.exit(0)
    
    curses.endwin()
    sys.exit(0)
