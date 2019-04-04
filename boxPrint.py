#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def boxPrint(symbol, width, heigth):
    """TODO: Docstring for boxPrint.
    """
    if len(symbol) != 1:
        raise Exception('Symbol must be a single character string.')
    if width <= 2:
        raise Exception('Width must be greater than 2.')
    if heigth <= 2:
        raise Exception('Heigth must be greater than 2.')
    print(symbol * width)
    for i in range(heigth - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)

for sym, w, h in (('*', 4, 4), ('0', 20, 5), ('x', 1, 3), ('ZZ', 3, 3),):
    try:
        boxPrint(sym, w, h)
    except Exception as e:
        print('An exception happened: ' + str(e))
