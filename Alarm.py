#Alarm function

import sys                          #System library
import curses                       #UI Library
import json                         #Json library

from time import sleep              #Wait function
from notifypy import Notify         #Notification library
from datetime import datetime       #System time
from os import getenv               #Environment function

def alarm(windowSize, modifyAlarms):
    #Make alarm window inside the main window
    AlarmWin = curses.newwin(windowSize[1]-2, windowSize[0]-2, 1, 1)
    AlarmWin.keypad(True)

    #Loads json file
    location = str(getenv("HOME")) + "/.config/PyClock_alarms.json"
    data = open(location, "r")
    alarms = json.load(data)
    data.close()
    option_x = 1
    option_y = 1

    #Creates alarms list
    alarms_list = []
    for obj in alarms:
        alarms_list.append(obj)
    attr_list = list(alarms[alarms_list[0]].keys())

    #Check flag to enter edit mode
    if modifyAlarms == True:
       while True:
            #Creates window box
            AlarmWin.clear()
            AlarmWin.attroff(curses.A_STANDOUT)
            AlarmWin.box()
            AlarmWin.addstr(0, 1, "Alarm")

            #Sets options name
            AlarmWin.attron(curses.A_STANDOUT)
            blank = " " * 44
            AlarmWin.addstr(1, 1, "Hour" + blank)
            blank = " " * 43
            AlarmWin.addstr(1, 49, "Title" + blank)
            blank = " " * 37
            AlarmWin.addstr(1, 97, "Description" + blank)
            blank = " " * 44
            AlarmWin.addstr(1, 145, "Icon" + blank)
            blank = " " * (windowSize[0] - 193 - 8)
            AlarmWin.addstr(1, 193, "Audio" + blank)
            AlarmWin.attroff(curses.A_STANDOUT)

            #Sets coordinates variables
            x = 1
            y = 3

            index = option_y-1
            #Loop through alarms
            for obj in alarms:
                #Quits if out of alarms
                if index >= len(alarms_list):
                    break
                #Loops through the alarm attributes
                for attr in alarms[obj]:
                    if alarms[alarms_list[index]][attr] == None:
                        continue
                    #Highlight selected option
                    if (option_x == x) and (option_y == index+1):
                        AlarmWin.attron(curses.A_STANDOUT)
                    else:
                        AlarmWin.attroff(curses.A_STANDOUT)

                    AlarmWin.addnstr(y, x, alarms[alarms_list[index]][attr], 47)
                    x = x + 48
                x = 1
                y = y + 1
                index = index + 1
                
                #Quits printing items if out of screen
                if y == windowSize[1]-3:
                    break

            AlarmWin.refresh()

            key = AlarmWin.getch()
            if key == curses.KEY_DOWN:
                option_y = 1 if option_y == len(alarms_list) else option_y+1
            
            elif key == curses.KEY_RIGHT:
                option_x = 1 if option_x == 193 else option_x+48

            elif key == curses.KEY_UP:
                option_y = len(alarms_list) if option_y == 1 else option_y-1

            elif key == curses.KEY_LEFT:
                option_x = 193 if option_x == 1 else option_x-48

            #Escape
            elif key == 27:
                curses.endwin()
                sys.exit(0)

            #Enter
            elif key == 10:
                #Clears option space
                buffer = " " * 48
                AlarmWin.addstr(3, option_x, buffer)
                AlarmWin.refresh()
                
                #Sets value for iteration
                buffer = ""
                char = AlarmWin.getch()
                char_n = 1
                while (not char == 27) and (char_n < 48):
                    if char == curses.KEY_BACKSPACE and char_n == 1:
                        char = AlarmWin.getch()
                        continue
                    elif char == curses.KEY_BACKSPACE and char_n > 1:
                        #Delete last char
                        buffer = buffer[:-1]
                        char_n = char_n - 1
                        char = AlarmWin.getch()
                        continue
                    #Adds char to string
                    buffer = buffer + chr(char)
                    AlarmWin.addnstr(3, option_x, buffer, len(buffer))
                    char = AlarmWin.getch()
                    char_n = char_n + 1

                #Adds the string and saves to json
                if option_x == 1:
                    alarms[alarms_list[option_y-1]][attr_list[0]] = buffer
                else:
                    alarms[alarms_list[option_y-1]][attr_list[int((option_x-1)/48)]] = buffer
                j_file = open(location, "w")
                json.dump(alarms, j_file)
                j_file.close()

            elif key == curses.KEY_BACKSPACE:
                #Creates new json obj
                item_name = "time" + str(len(alarms_list)+1)
                new_dict = {"hour":"00:00", "title":"", "desc":"", "icon":"", "audio":""}
                alarms[item_name] = new_dict
                j_file = open(location, "w")
                json.dump(alarms, j_file)
                j_file.close()
                curses.endwin()
                sys.exit(0)

            #Tab
            elif key == 9:
                #Deletes selected json obj
                item_name = "time" + str(option_y)
                alarms.pop(item_name)
                alarms_list.remove(item_name)
                new_index = 1
                #Loops through the remaining obj
                for alarm in alarms_list:
                    #Renames obj
                    item_name = "time" + str(new_index)
                    alarms[item_name] = alarms.pop(alarm)
                    new_index = new_index + 1
                j_file = open(location, "w")
                json.dump(alarms, j_file)
                j_file.close()
                curses.endwin()
                sys.exit(0)

        
    #Enters alarm mode
    curses.endwin()
    while True:
        time = datetime.now().strftime("%H:%M")
        notifier = Notify()
        for alarm in alarms_list:
            if time == alarms[alarm]["hour"]:
                #Sets title
                if alarms[alarm]["title"] != "":
                    notifier.title = alarms[alarm]["title"]
                else:
                    notifier.title = "PyClock"

                #Sets description
                if alarms[alarm]["desc"] != "":
                    notifier.message = alarms[alarm]["desc"]
                else:
                    notifier.message = alarms[alarm]["hour"]

                #Sets icon
                if alarms[alarm]["icon"] != "":
                    notifier.icon = alarms[alarm]["icon"]
                else:
                    notifier.icon = str(getenv("HOME")) + "/.config/PyClock_icon.ico"
                
                #Sets audio
                if alarms[alarm]["audio"] == "Yes":
                    notifier.audio = str(getenv("HOME")) + "/.config/PyClock_audio.wav"

                notifier.send()

        del notifier
        sleep(60)
