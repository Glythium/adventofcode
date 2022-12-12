#!/usr/bin/python3


def findRanges(line):
    first, second = line.split(",")
    return getRanges(first), getRanges(second)


def getRanges(pair):
    left, right = pair.split("-")
    return range(int(left), int(right) + 1)


def listToSet(inRange):
    newSet = set()
    for i in inRange:
        newSet.add(i)
    return newSet


def doesContain(first, second):
    if len(first.difference(second)) == 0:
        return True
    return False


def containsAtAll(first, second):
    if len(first.difference(second)) < len(first):
        return True
    return False


def dedupeAssignments(cleanupAssignments):
    allOverlapping = 0
    anyOverlapping = 0

    for line in cleanupAssignments:
        firstRange, secondRange = findRanges(line)
        firstSet = listToSet(firstRange)
        secondSet = listToSet(secondRange)
        if doesContain(firstSet, secondSet) or doesContain(secondSet, firstSet):
            allOverlapping += 1
            anyOverlapping += 1
        elif containsAtAll(firstSet, secondSet) or containsAtAll(secondSet, firstSet):
            anyOverlapping += 1

    return allOverlapping, anyOverlapping


if __name__ == "__main__":
    print("Please use the main.py script instead of this one directly")
