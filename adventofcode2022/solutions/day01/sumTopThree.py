#!/usr/bin/python3


def sumTopThreeCalories(calList):
    totalCals = []
    curCals = 0
    sumCals = 0

    for line in calList:
        item = line.strip()
        if item == "":
            totalCals.append(curCals) 
            curCals = 0
            continue
        curCals += int(item)
    
    totalCals.sort()
    topThree = totalCals[-3:]

    for i in topThree:
        sumCals += i
    
    return sumCals


if __name__ == "__main__":
    print("Please use the main.py script instead of this one directly")