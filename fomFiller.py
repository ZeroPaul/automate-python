#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pyautogui as pag
import time

nameField = (648, 319)
submitButton = (651, 817)
submitButtonColor = (75, 141, 249)
submitAnotherLink = (760, 224)

formData = [{'name': 'Alice', 'fear': 'eavesdroppers', 'source': 'wand', 
            'robocop': 4, 'comments': 'Tell Bob I said hi.'},
            {'name': 'Bob', 'fear': 'bees', 'source': 'amulet', 'robocop': 4,
            'comments': 'n/a'},{'name': 'Carol', 'fear': 'puppets', 
            'source':'crystal ball', 'robocop': 1, 'comments': 'Please take \
            the puppets out of the break room.'},
            {'name': 'Alex Murphy', 'fear': 'ED-209', 'source': 'money',
            'robocop': 5, 'comments': 'Protect the innocent. Serve the public \
            trust. Uphold the law.'},
            ]
for person in formData:
    print('>>> 5 SECONDS PAUSE TO LET USER PRESS CTRL-C')
    time.sleep(5)

    while not pag.pixelMatchesColor(submitButton[0], submitButton[1],
            submitButtonColor):
        time.sleep(0.5)

    print('Entering %s info...' % (person['name']))
    pag.click(nameField[0], nameField[1])
    pag.typewrite(person['name'] + '\t')
    pag.typewrite(person['fear'] + '\t')

    if person['source'] == 'wand':
        pag.typewrite(['down', '\t'])
    elif person['source'] == 'amulet':
        pag.typewrite(['down', 'down', '\t'])
    elif person['source'] == 'crystal ball':
        pyautogui.typewrite(['down', 'down', 'down', '\t'])
    elif person['source'] == 'money':
        pag.typewrite(['down', 'down', 'down', 'down', '\t'])

    if person['robocop'] == 1:
        pag.typewrite([' ', '\t'])
    elif person['robocop'] == 2:
        pag.typewrite(['right', '\t'])
    elif person['robocop'] == 3:
        pag.typewrite(['right', 'right', '\t'])
    elif person['robocop'] == 4:
        pag.typewrite(['right', 'right', 'right', '\t'])
    elif person['robocop'] == 5:
        pag.typewrite(['right', 'right', 'right', 'right', '\t'])

    pag.typewrite(person['comments'] + '\t')

    pag.PRESS('enter')
    print('Clicked Submit.')
    time.sleep(5)

    pag.click(submitAnotherLink[0], submitAnotherLink[1])

