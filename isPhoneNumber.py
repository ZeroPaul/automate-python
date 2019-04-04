#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def isPhoneNumber(text):
    """TODO: Docstring for isPhoneNumber.
    """
    if len(text) != 12:
        return False
    for i in range (0, 3):
        if not text[i].isdecimal():
            return False
    
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False

    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

print('415-555-4242 is phone number:')
print(isPhoneNumber('415-555-4242'))
print('Moshi mosh is phone number:')
print(isPhoneNumber('Moshi mosh'))

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
print('Done')
