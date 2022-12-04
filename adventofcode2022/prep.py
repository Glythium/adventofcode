#!/usr/bin/python3

from helpers import getAdventInput
from solutions.day01.countCalories import countCalories
from solutions.day01.sumTopThree import sumTopThreeCalories
from solutions.day02.scoreRPS import scoreRPS


def solveDay01():
    inputFile = "inputs/calories.txt"
    calList = getAdventInput(inputFile)
    
    return countCalories(calList), sumTopThreeCalories(calList)


def solveDay02():
    inputFile = "inputs/rps-strategy-guide.txt"
    rpsList = getAdventInput(inputFile)

    return scoreRPS(rpsList)


if __name__ == "__main__":
    print("Please use the main.py script instead of this one directly")