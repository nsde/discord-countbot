"""
"""


import sys
import time
import mouse
import random
import keyboard

safe_mode = True # delay between switching accounts

def send(count):
    keyboard.write(str(count))
    keyboard.press_and_release('enter')

def switch():
    # mouse.click()
    keyboard.press('alt')
    time.sleep(0.1)
    keyboard.press('tab')
    time.sleep(0.1)
    keyboard.release('alt')
    time.sleep(0.1)
    keyboard.release('tab')

    if safe_mode:
        time.sleep(random.randint(1, 2))

count = int(input('Current count: '))
print('Press shift to start, esc to stop.')
keyboard.wait('shift')
time.sleep(1)

while 1:
    count += 1

    send(count=count)
    print(count) 
    switch()
    print('Switching')
