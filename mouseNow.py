#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pyautogui as pag
#pip install PyAutoGUI

print('Press Ctrl-C to quit.')

try:
    while True:
        x, y = pag.position()
        positionStr = 'X: ' + str(x).rjust(4) + 'Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt as e:
    print('\nDone.')


