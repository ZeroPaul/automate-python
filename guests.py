#!/usr/bin/env python3
# -*- coding: utf-8 -*-

allGuests = {'Alice': {'apples': 5, 'pretsels': 12,},
             'Bob': {'ham sandwiches': 3, 'apples': 2,},
             'Carol': {'cups': 3, 'apple pies': 1,},
             }

def totalBrought(guest, item):
    """TODO: Docstring for totalBrought.
    """
    numBrougth = 0
    for k, v in guest.items():
        numBrougth = numBrougth + v.get(item, 0)
    return numBrougth

print('Number of things being brought:')
print(' - Apples            ' + str (totalBrought(allGuests, 'apples')))
print(' - Cups              ' + str (totalBrought(allGuests, 'cups')))
print(' - Cakes             ' + str (totalBrought(allGuests, 'cakes')))
print(' - Ham Sandwiches    ' + str (totalBrought(allGuests, 'ham sandwiches')))
print(' - Apple Pies            ' + str (totalBrought(allGuests, 'apple pies')))

