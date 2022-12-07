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


def findBadge(first, second, third):
    # Really making me want to refactor this and findDuplicate
    # to create a function that searches through a list of lists
    for c in first:
        if c in second and c in third:
            return c

    # Returning the empty string on failure
    return ''


def calculatePriority(duplicateChar):
    LOWERCASE_OFFSET = 96
    UPPERCASE_OFFSET = 38
    offset = 0

    if duplicateChar.islower():
        offset = LOWERCASE_OFFSET
    elif duplicateChar.isupper():
        offset = UPPERCASE_OFFSET
    else:
        print("The duplicate character was not upper/lower cased!")
        sys.exit(1)

    return ord(duplicateChar) - offset


def partOne(ruckList):
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

        totalPriority += calculatePriority(duplicateChar)

    return totalPriority


def partTwo(ruckList):
    totalPriority = 0
    duplicateChar = ''

    # Absolutely a better way to grab three lines
    count = 0
    groupsOfThree = []
    for line in ruckList:
        # Fill the buffer list with three strings
        groupsOfThree.append(line.strip())
        count += 1
        if count == 3:
            # Unpacking for readable vars beyond just indexing the list
            first, second, third = groupsOfThree

            duplicateChar = findBadge(first, second, third)
            if duplicateChar == '':
                print("No duplicate char found!")
                sys.exit(1)

            totalPriority += calculatePriority(duplicateChar)

            # Reset the count and buffer list to get ready for the next three
            groupsOfThree = []
            count = 0

    return totalPriority


def checkRucks(ruckList):
    return partOne(ruckList), partTwo(ruckList)


if __name__ == "__main__":
    print("Please use the main.py script instead of this one directly")
