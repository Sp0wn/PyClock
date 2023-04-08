#String to ASCII art function

from os import getenv       #Environment function

def convert_numbers(timeStr):
    #Use logic to find the numbers style file 
    location = str(getenv("HOME")) + "/.config/PyClock_numbers.config"
    file = open(location, "r")

    number = []
    cache = []

    #Read through the file
    for line in file:
        #Stops reading at newline
        if line == "\n":
            #Adds the number array and resets
            cache.append(number)
            number = []
            continue
        #Cleans string and adds it
        line = line.strip("\n")
        number.append(line)

    ascii_arr = []

    #Loops through the time string
    for ch in timeStr:
        #Converts special character
        if ch == ":":
            ascii_arr.append(cache[10])
            continue
        #Converts number
        ascii_arr.append(cache[int(ch)])
    
    file.close()

    return ascii_arr
