#!/usr/bin/python3

import sys


def splitCompartments(line):
    # Have to int() this because Python wants to give floats during division
    halfLen = int(len(line) / 2)

    # Returns a list containing two halves of a string
    return [line[:halfLen], line[halfLen:]]


def findRepeat(stringList):
    if len(stringList) < 2:
        print("Can't find repeats with only one string!")
        return ''

    repeatChar = ''

    # Finds a character that exists across all strings in a list
    for character in stringList[0]:
        for otherString in stringList[1:]:
            if character in otherString:
                repeatChar = character
            else:
                # This is not the character you're looking for
                repeatChar = ''
                break

        if repeatChar != '':
            # We found the character that exists in all other strings
            break

    # Expect the empty string on failure
    return repeatChar


def calculatePriority(duplicateChar):
    # The ASCII value of ('a' - LOWERCASE_OFFSET) = 1
    LOWERCASE_OFFSET = 96

    # The ASCII value of ('A' - UPPERCASE_OFFSET) = 27
    UPPERCASE_OFFSET = 38

    offset = 0

    if duplicateChar.islower():
        offset = LOWERCASE_OFFSET
    elif duplicateChar.isupper():
        offset = UPPERCASE_OFFSET
    else:
        print("The duplicate character was not upper/lower cased!")
        sys.exit(1)

    # ord(X) returns the ASCII value of a given character
    return ord(duplicateChar) - offset


def partOne(ruckList):
    totalPriority = 0

    for line in ruckList:
        duplicateChar = findRepeat(splitCompartments(line))
        if duplicateChar == '':
            print("No duplicate character found!")
            sys.exit(1)

        totalPriority += calculatePriority(duplicateChar)

    return totalPriority


def partTwo(ruckList):
    totalPriority = 0
    duplicateChar = ''

    # Absolutely a better way to grab three lines
    count = 0
    groupOfThree = []
    for line in ruckList:
        # Fill the buffer list with three strings
        groupOfThree.append(line.strip())
        count += 1
        if count == 3:
            duplicateChar = findRepeat(groupOfThree)
            if duplicateChar == '':
                print("No duplicate char found!")
                sys.exit(1)

            totalPriority += calculatePriority(duplicateChar)

            # Reset the count and buffer list to get ready for the next three
            groupOfThree = []
            count = 0

    return totalPriority


def checkRucks(ruckList):
    return partOne(ruckList), partTwo(ruckList)


if __name__ == "__main__":
    print("Please use the main.py script instead of this one directly")
