#!/usr/bin/python
import numpy, pprint, sys, Queue
from assets import loadLetters

def printBanner(banner):
    for i in range(0, 7):
        row = ""
        for j in range(0, len(banner[0])):
            num = int(banner[i][j])
            if num == 0:
                row += " "
            else:
                row += u"\u2588"
        print row

def sim(text):
    letters = loadLetters()
    banner = numpy.zeros((7, (len(text) * 6)))

    column = 0
    for i in range(0, len(text)):
        letter = letters[ord(text[i])]
        for j in range(0, 7):
            for k in range(0, 5):
                banner[j][k + column] = letter[j][k]
        column += 6
    
    printBanner(banner)

sim("OAKLEY")
