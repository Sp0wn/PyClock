#PyClock

from Clock import Clock
from Timer import Timer

import sys

if __name__ == "__main__":

    YELLOW = "\x1b[33m"
    RED = "\x1b[31m"
    END = "\x1b[0m"

    Err1 = "Err: Too few arguments"
    Err2 = "Err: Wrong arguments"

    if len(sys.argv) < 2:
        print(RED + Err1 + END)
        sys.exit(1)

    if sys.argv[1] == "-h" or sys.argv[1] == "--help":
        print(YELLOW, end = "")
        print("Usage: PyClock -m <mode> <args>")
        print("Modes: Clock (c), Timer (t), Alarm (a), Stopwatch (s)")
        print("Clock: ... {Hour format} (12 || 24) {Add seconds} (1 || 0)")
        print(END, end = "")
    
    elif sys.argv[1] == "-m":
        if len(sys.argv) < 3:
            print(RED + Err1 + END)
            sys.exit(1)

        if sys.argv[2] == "Clock" or sys.argv[2] == "c":
            if len(sys.argv) < 4:
                print(RED + Err1 + END)
                sys.exit(1)

            else:
                hourFormat = sys.argv[3]
                if len(sys.argv) > 4:
                    addSeconds = sys.argv[4]
                    Clock(hourFormat, addSeconds)

                else:
                    print(RED + Err1 + END)
                    sys.exit(1)

        elif sys.argv[2] == "Timer" or sys.argv[2] == "t":
            if len(sys.argv) < 4:
                print(RED + Err1 + END)
                sys.exit(1)

            else:
                seconds = sys.argv[3]
                Timer(seconds)


        else:
            print(RED + Err2 + END)
            sys.exit(1)
    
    else:
        print(RED + Err2 + END)
        sys.exit(1)
