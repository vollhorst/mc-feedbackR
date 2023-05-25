#!/bin/python
# quelle:
# https://stackoverflow.com/questions/38507426/image-to-text-python

import sys
from PIL import Image
from pytesseract import image_to_string


def bild_zu_text(bild):
    bild = Image.open(bild, mode='r')
    text = image_to_string(bild, lang='deu')
    return text


print(bild_zu_text(sys.argv[1]))

# ende.

