#Counter function

import sys                          #System library
import curses                       #UI Library

from datetime import timedelta      #Time diff
from ASCII import convert_numbers   #ASCII Art

def counter(countdownSeconds, windowSize):
    #Make timer window in the middle of the screen
    CounterWin = curses.newwin(7, 66, round(windowSize[1]/2)-8, round(windowSize[0]/2)-32)
    CounterWin.keypad(True)
    CounterWin.timeout(1000)

    #Start countdown before counter
    if not countdownSeconds == None:
        countdownFormat = timedelta(seconds=countdownSeconds)
        countdown = int(countdownFormat.total_seconds())
        while countdown >= 0:
            #Creates window box
            CounterWin.clear()
            CounterWin.box()
            CounterWin.addstr(0, 1, "Counter")

            #Adds zero at the start of the string
            countdownFormat = str(countdownFormat)
            if len(countdownFormat) < 8:
                countdownFormat = "0" + countdownFormat
                
            #Sets coordinates variables
            x = 1
            y = 1

            #Get the ascii art array
            asciiNumbers = convert_numbers(countdownFormat)
            #Loop through the array of arrays
            for arr in asciiNumbers:
                for line in arr:
                    CounterWin.addstr(y, x, line)
                    y = y + 1
                x = x + 8
                y = 1

            #Decreases countdown by one second
            countdown = countdown - 1
            countdownFormat = timedelta(seconds=countdown)

            CounterWin.refresh()

            #Checks for esc key
            key = CounterWin.getch()
            if key == 27:
                curses.endwin()
                sys.exit(0)

    #Sets counter
    counter_n = 0
    counterFormat = timedelta(seconds=counter_n)

    #Loops through time
    while True:
        #Creates window box
        CounterWin.clear()
        CounterWin.box()
        CounterWin.addstr(0, 1, "Counter")
   
        #Adds zero at the start of the string
        counterFormat = str(counterFormat)
        if len(counterFormat) < 8:
            counterFormat = "0" + counterFormat

        #Sets coordinates variables
        x = 1
        y = 1

        #Get the ascii art array
        asciiNumbers = convert_numbers(counterFormat)
        #Loop through the array of arrays
        for arr in asciiNumbers:
            for line in arr:
                CounterWin.addstr(y, x, line)
                y = y + 1
            x = x + 8
            y = 1

        #Increases counter by one second
        counter_n = counter_n + 1
        counterFormat = timedelta(seconds=counter_n)

        CounterWin.refresh()
    
        #Checks for esc key
        key = CounterWin.getch()
        if key == 27:
            curses.endwin()
            sys.exit(0)
