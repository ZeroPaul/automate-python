#!/usr/bin/env python3
# -*- coding: utf-8 -*-


while True:
    print('Enter your age:')
    age = input()
    if age.isdecimal():
        break
    print('Please enter a numer for your age.')

while True:
    print('Select a new password (letters and numbers only):')
    password = input()
    if password.isalnum():
        break
    print('Passwords can only have letters and numbers.') 

    
