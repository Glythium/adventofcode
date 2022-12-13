#!/usr/bin/python3

from helpers import getAdventInput
from solutions.day01.countCalories import countCalories
from solutions.day01.sumTopThree import sumTopThreeCalories
from solutions.day02.scoreRPS import playRPS, fixRPS
from solutions.day03.checkRucks import checkRucks
from solutions.day04.dedupeAssignments import dedupeAssignments
from solutions.day05.moveCargo import moveCargo


def solveDay01():
    calList = getAdventInput("inputs/calories.txt")

    return countCalories(calList), sumTopThreeCalories(calList)


def solveDay02():
    rpsList = getAdventInput("inputs/rps-strategy-guide.txt")

    return playRPS(rpsList), fixRPS(rpsList)


def solveDay03():
    ruckList = getAdventInput("inputs/rucksack-compartments.txt")

    return checkRucks(ruckList)


def solveDay04():
    cleanupAssignments = getAdventInput("inputs/cleanup-assignments.txt")

    return dedupeAssignments(cleanupAssignments)


def solveDay05():
    cargoInput = getAdventInput("inputs/cargo-setup.txt")

    return moveCargo(cargoInput)


if __name__ == "__main__":
    print("Please use the main.py script instead of this one directly")
