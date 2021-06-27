# Melissa J Johnson
# 06/27/2021

# Create your own Pomodoro timer

from datetime import timedelta, datetime

import time
import subprocess


def beep():
    subprocess.call(["afplay", "beep_beep.wav"])


timer_length = input("Set timer (mins): ")

timer_seconds = int(timer_length) * 60

while True:
    print(timedelta(seconds=timer_seconds))
    timer_seconds -= 1
    if timer_seconds < 0:
        for i in range(10):
            beep()

        break
    time.sleep(1)

print("Beep beep! time is up!")
