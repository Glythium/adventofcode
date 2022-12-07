#!/usr/bin/python3


def countCalories(calList):
    curCals = 0
    maxCals = 0

    for line in calList:
        item = line.strip()
        if item == "":
            if curCals > maxCals:
                maxCals = curCals
            curCals = 0
            continue
        curCals += int(item)

    return maxCals


if __name__ == "__main__":
    print("Please use the main.py script instead of this one directly")