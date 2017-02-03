#!/usr/bin/python
import sys
from communication import updateBanner, getBanner

def printBreak():
    print "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - "

def displayOptions(code):
    if code == 1:
        printBreak()
        print "Invalid option."
        printBreak()

    print "(1) Update Banner Text"
    print "(2) Retrieve Banner Text"
    print "(3) Simulate Banner"
    print "(4) Exit"
    printBreak()

    response = raw_input("Please enter an option: ")
    response = int(response)

    if response == 1:
        newBanner = raw_input("Please enter the new banner: ")
        updateBanner(newBanner)
        displayOptions(0)
    elif response == 2:
        banner = getBanner()
        print "Current Banner: " + banner
        displayOptions(0)
    elif response == 3:
        print "Simulate"
    elif response == 4:
        sys.exit()
    else:
        displayOptions(1)

displayOptions(0)
