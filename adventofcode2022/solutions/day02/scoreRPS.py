#!/usr/bin/python3


def scoreRPS(rpsList):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3
    LOSE = 0
    DRAW = 3
    WIN = 6

    rps = {"X": "A", "Y": "B", "Z": "C"}
    totalScore = 0

    for line in rpsList:
        opp, you = line.split()
        # TODO: the rest



if __name__ == "__main__":
    print("Please use the main.py script instead of this one directly")