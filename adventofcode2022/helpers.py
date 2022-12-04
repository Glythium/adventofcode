#!/usr/bin/python3


def getAdventInput(inputFile):
    lines = []

    try:
        with open(inputFile, "r") as fp:
            lines = fp.readlines()
    except FileNotFoundError:
        print("Could not find file {}".format(inputFile))
        return None
    
    return lines


if __name__ == "__main__":
    print("Please use the main.py script instead of this one directly")