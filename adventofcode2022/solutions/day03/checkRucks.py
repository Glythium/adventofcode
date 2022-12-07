#!/usr/bin/python3

import sys


def splitCompartments(line):
    # Have to int() this because Python wants to give floats during division
    halfLen = int(len(line) / 2)

    return line[:halfLen], line[halfLen:]


def sortUpperLower(letters):
    lower = []
    upper = []

    for c in letters.strip():
        if c.islower():
            lower.append(c)
        else:
            upper.append(c)

    lower.sort()
    upper.sort()
    return lower, upper


def findDuplicate(left, right):
    # There's absolutely a better way to do this
    for c in left:
        if c in right:
            return c

    # Returning the empty string on failure
    return ''


def checkRucks(ruckList):
    LOWERCASE_OFFSET = 96
    UPPERCASE_OFFSET = 38
    totalPriority = 0

    for line in ruckList:
        left, right = splitCompartments(line)
        lowerL, upperL = sortUpperLower(left)
        lowerR, upperR = sortUpperLower(right)

        duplicateChar = ''
        # Two function calls to keep the findDuplicate function more generic;
        # operating against two strings instead of a function requiring four
        # strings which seems very specific.
        duplicateChar = findDuplicate(lowerL, lowerR)
        if duplicateChar == '':
            duplicateChar = findDuplicate(upperL, upperR)
            if duplicateChar == '':
                # Something went horribly wrong
                print("No duplicate character found!")
                sys.exit(1)

        offset = 0
        if duplicateChar.islower():
            offset = LOWERCASE_OFFSET
        elif duplicateChar.isupper():
            offset = UPPERCASE_OFFSET
        else:
            print("The duplicate character was not upper/lower cased!")
            sys.exit(1)

        totalPriority += ord(duplicateChar) - offset

    return totalPriority


if __name__ == "__main__":
    print("Please use the main.py script instead of this one directly")
