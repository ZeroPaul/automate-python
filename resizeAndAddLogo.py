#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from PIL import Image

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'catlogo.png'

logoIm = Image.open(LOGO_FILENAME)
logoWidth, logoHeight = logoIm.size

os.makedirs('withlogo', exist_ok=True)

for filename in os.listdir('.'):
    if not (filename.endswith('.png') or filename.endswith('jpg') or filename \
        == LOGO_FILENAME):
        continue

    im = Image.open(filename)
    width, heigth = im.size

    if width > SQUARE_FIT_SIZE and heigth > SQUARE_FIT_SIZE:
        if width > heigth:
            heigth = int((SQUARE_FIT_SIZE / width) * heigth)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE / heigth) * width)
            heigth = SQUARE_FIT_SIZE

        print('Resizing %s...' % (filename))
        im = im.resize((width, heigth))

    print('Adding logo to  %s...' % (filename))
    im.paste(logoIm, (width - logoWidth, heigth - logoHeight), logoIm)

    im.save(os.path.join('', filename))

