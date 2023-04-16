import  os

location = str(os.getenv("HOME")) + "/.config"

os.system("pip install notify-py")
os.system("pip install pyinstaller")

os.system("python -m PyInstaller --onefile --windowed PyClock.py")
os.system("mv dist/PyClock .")
os.system("sudo chmod a+x ./PyClock")
os.system("sudo mv PyClock /usr/local/bin")

os.system("cp files/PyClock_alarms.json " + location)
os.system("cp files/PyClock_icon.ico " + location)
os.system("cp files/PyClock_numbers.config " + location)
os.system("cp files/PyClock_sound.wav" + location)

os.system("rm -rf dist/")
os.system("rm -rf build/")
os.system("rm PyClock.spec")
