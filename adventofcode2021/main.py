#!/usr/bin/python3

from classes import Submarine
from libs import getInput
from day_03 import day_3

def solveDay3(mySub):
    data = getInput.getInput("day_03/input.txt")
    day_3.part1(mySub, data)

def main():
    mySub = Submarine.Submarine()
    solveDay3(mySub)

if __name__ == '__main__':
    main()