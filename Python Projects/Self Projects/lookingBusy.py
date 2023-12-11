#! python3
# lookingBusy.py - A program to fool people into thinking I'm online. (SCRATCH)

import pyautogui
import sys

print('Now starting to look busy... Press Ctrl-C when you want to stop \
the program!')

while True:  # Loop program indefinitely.
    try:
        pyautogui.move(-10, 0, 0.5)  # Make mouse move to the left.
        pyautogui.sleep(10)          # Pause for 10 seconds.
        pyautogui.move(10, 0, 0.5)   # Make mouse move to the right.
        pyautogui.sleep(10)          # Pause for 10 seconds again.
    except KeyboardInterrupt:  # Ctrl-C exception.
        print('See you! Press Y then ENTER to confirm you want to exit. :]')
        sys.exit()
