#PyClock

import argparse         #CLI Parser

def main():
    parser = argparse.ArgumentParser(
                        prog="PyClock", 
                        description="Terminal multifuncion clock",)

    subparsers = parser.add_subparsers(required=True, metavar="Command", dest="cmd")
    parser_clock = subparsers.add_parser("Clock", help="Clock --help")
    parser_alarm = subparsers.add_parser("Alarm", help="Alarm --help")
    parser_timer = subparsers.add_parser("Timer", help="Timer --help")
    parser_counter = subparsers.add_parser("Counter", help="Counter --help")

    parser_clock.add_argument("--hour-format", choices=[12, 24], type=int)
    parser_clock.add_argument("--add-seconds", action="store_true")
    parser_alarm.add_argument("--modify-alarms", action="store_true")
    parser_timer.add_argument("--time-unit", required=True, action="append", choices=["s", "m", "h"])
    parser_timer.add_argument("--time-value", required=True, action="append", type=int)
    parser_counter.add_argument("--countdown", type=int)

    args = vars(parser.parse_args())
    cmd = args["cmd"]

if __name__ == "__main__":
    main()
