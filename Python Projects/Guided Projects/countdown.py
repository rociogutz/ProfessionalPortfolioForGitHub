#! python3
# countdown.py - A simple countdown script.

import time, subprocess, os

os.chdir('C:\\Windows\\Media') # found out you have to play .wav from its path

timeLeft = 10
while timeLeft > 0:
    print(timeLeft, end='\n')
    time.sleep(1)
    timeLeft = timeLeft - 1

# At the end of the countdown, play a sound file.
subprocess.Popen(['start', 'notify.wav'], shell=True)
