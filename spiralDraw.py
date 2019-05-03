#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pyautogui as pag
import time

time.sleep(5)
pag.click()
distance = 200
while distance > 0:
    pag.dragRel(distance, 0, duration=0.2)
    distance = distance - 5
    pag.dragRel(0, distance, duration=0.2)
    pag.dragRel(-distance, 0, duration=0.2)
    distance = distance - 5
    pag.dragRel(0, -distance, duration=0.2)

#After open https://sketch.io/sketchpad/

