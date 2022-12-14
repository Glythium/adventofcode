#!/usr/bin/python3


def hasRepeats(buffer):
    checkSet = set()

    # Adding the chars to a set will eliminate repeats
    for c in buffer:
        checkSet.add(c)
    
    # If there were characters repeated
    if len(checkSet) < len(buffer):
        # Then the set length will be smaller than the buffer was
        return True
    
    return False


def findMarker(datastream, windowSize):
    index = 0

    for i, c in enumerate(datastream):
        buffer = datastream[i: i + windowSize]
        if not hasRepeats(buffer):
            index = i + windowSize
            break

    return index


def parseDatastream(datastream):
    # The datastream comes in as a list, but it's just one item long
    datastream = datastream[0]

    index = findMarker(datastream, 4)
    indexTwo = findMarker(datastream, 14)

    return index, indexTwo


if __name__ == "__main__":
    print("Please use the main.py script instead of this one directly")