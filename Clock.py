#Clock function

from datetime import datetime
from time import sleep
from art import tprint

import signal
import sys
import os

def Clock(hourFormat, secondsTrue):
    def handler(signum, frame):
        end = input(YELLOW + "\nDo you want to exit?[Y/n]: " + END)

        if end == "Y" or end == "":
            sys.exit(0)

    signal.signal(signal.SIGINT, handler)
    
    YELLOW = "\x1b[33m"
    BLUE = "\x1b[34m"
    RED = "\x1b[31m"
    END = "\x1b[0m"

    Err1 = "Err: Invalid format"
    Err2 = "Err: Invalid value"

    while(True):
        if secondsTrue == "1":
            if hourFormat == "12":
                time = datetime.now().strftime("%I:%M:%S")

            elif hourFormat == "24":
                time = datetime.now().strftime("%H:%M:%S")

            else:
                print(RED + Err1 + END)
                sys.exit(1)

        elif secondsTrue == "0":
            if hourFormat == "12":
                time = datetime.now().strftime("%I:%M")

            elif hourFormat == "24":
                time = datetime.now().strftime("%H:%M")

            else:
                print(RED + Err1 + END)
                sys.exit(1)
        
        else:
            print(RED + Err2 + END)
            sys.exit(1)

        os.system("clear")
        print(BLUE, end = "")
        tprint(time)
        print(END, end = "")
        sleep(1)
