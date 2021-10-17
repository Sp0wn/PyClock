#Timer function

from datetime import timedelta
from time import sleep
from art import tprint

import signal
import sys
import os

def Timer(timeSeconds):
    def handler(signum, frame):
        end = input(YELLOW + "\nDo you want to exit?[Y/n]: " + END)

        if end == "Y" or end == "":
            sys.exit(0)

    signal.signal(signal.SIGINT, handler)

    YELLOW = "\x1b[33m"
    BLUE = "\x1b[34m"
    RED = "\x1b[31m"
    END = "\x1b[0m"

    Err1 = "Err: Not a number"
    Err2 = "Err: Invalid number"

    if timeSeconds.isdigit() == True:
        timeSeconds = int(timeSeconds)

    else:
        print(RED + Err1 + END)
        sys.exit(1)

    if timeSeconds >= 86400:
        print(RED + Err2 + END)
        sys.exit(1)

    while timeSeconds >= 0:
        os.system("clear")
        time = timedelta(seconds = timeSeconds)
        print(BLUE, end = "")
        tprint(str(time))
        timeSeconds = timeSeconds - 1
        print(END, end = "")
        sleep(1)
