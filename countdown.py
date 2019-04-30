#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import subprocess

timeLeft = 60
while timeLeft > 0:
    print(timeLeft, end='')
    time.sleep(1)
    timeLeft = timeLeft - 1

subprocess.Popen(['start', 'alarm.wav'], shell=True)

