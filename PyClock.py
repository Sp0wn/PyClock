#PyClock

import argparse         #CLI Parser
import curses           #UI Library

from Clock import clock
from Timer import timer
from Counter import counter
from Alarm import alarm

def main():
    #Initialize parser
    parser = argparse.ArgumentParser(
                        prog="PyClock", 
                        description="Terminal multifuncion clock")

    #Create commands
    subparsers = parser.add_subparsers(required=True, metavar="Command", dest="cmd")
    parser_clock = subparsers.add_parser("Clock", help="Clock --help")
    parser_alarm = subparsers.add_parser("Alarm", help="Alarm --help")
    parser_timer = subparsers.add_parser("Timer", help="Timer --help")
    parser_counter = subparsers.add_parser("Counter", help="Counter --help")

    #Create commands arguments
    parser_clock.add_argument("--hour-format", choices=[12, 24], type=int)
    parser_clock.add_argument("--add-seconds", action="store_true")
    parser_alarm.add_argument("--modify-alarms", action="store_true")
    parser_timer.add_argument("--time-unit", required=True, action="append", choices=["s", "m", "h"])
    parser_timer.add_argument("--time-value", required=True, action="append", type=int)
    parser_counter.add_argument("--countdown", type=int)

    #Get arguments value
    args = vars(parser.parse_args())
    cmd = args["cmd"]

    #Initialize main window
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)
    stdscr.clear()
    curses.curs_set(0)
    curses.start_color()
    curses.use_default_colors()

    curses.init_pair(1, curses.COLOR_GREEN, -1)
    curses.init_pair(2, curses.COLOR_BLUE, -1)

    stdscr.attron(curses.color_pair(1))
    stdscr.box()
    stdscr.addstr(0, 1, "PyClock")
    stdscr.refresh()
    stdscr.attroff(curses.color_pair(1))
    y, x = stdscr.getmaxyx()
    size = [x, y]

    if cmd == "Clock":
        if args["hour_format"] == None:
            args["hour_format"] = 12
        clock(args["hour_format"], args["add_seconds"], size)

    elif cmd == "Timer":
        timer(args["time_unit"], args["time_value"], size)

    elif cmd == "Counter":
        counter(args["countdown"], size)

    elif cmd == "Alarm":
        alarm(size, args["modify_alarms"])

if __name__ == "__main__":
    main()
