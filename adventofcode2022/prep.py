#!/usr/bin/python3

from helpers import getAdventInput
from solutions.day01.countCalories import countCalories
from solutions.day01.sumTopThree import sumTopThreeCalories
from solutions.day02.scoreRPS import playRPS, fixRPS


def solveDay01():
    calList = getAdventInput("inputs/calories.txt")
    
    return countCalories(calList), sumTopThreeCalories(calList)


def solveDay02():
    rpsList = getAdventInput("inputs/rps-strategy-guide.txt")

    return playRPS(rpsList), fixRPS(rpsList)


if __name__ == "__main__":
    print("Please use the main.py script instead of this one directly")