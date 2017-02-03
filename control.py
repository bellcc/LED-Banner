#!/usr/bin/python
import sys
from communication import updateBanner, getBanner
from assets import loadLetters

def printMessage(message):
    print "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - "
    print message
    print "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - "

def displayOptions():
    while True:
        print "(1) Update Banner Text"
        print "(2) Retrieve Banner Text"
        print "(3) Simulate Banner"
        print "(4) Exit"

        response = raw_input("Please enter an option: ")
        response = int(response)

        if response == 1:
            newBanner = raw_input("Please enter the new banner: ")
            updateBanner(newBanner)
        elif response == 2:
            banner = getBanner()
            printMessage("Current Banner: " + banner)
        elif response == 3:
            print "Simulate"
        elif response == 4:
            sys.exit()
        else:
            printMessage("Invalid Input. Try Again.")

displayOptions()
