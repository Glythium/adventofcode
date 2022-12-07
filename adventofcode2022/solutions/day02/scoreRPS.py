#!/usr/bin/python3

import sys


ROCK = 1
PAPER = 2
SCISSORS = 3


def scoreRPS(opp, you):
    LOSE = 0
    DRAW = 3
    WIN = 6

    score = 0
    rps = {
        "A": ROCK, "B": PAPER, "C": SCISSORS,
        "X": ROCK, "Y": PAPER, "Z": SCISSORS
    }

    # Check for a draw
    if rps[opp] == rps[you]:
        score += DRAW + rps[you]
    elif (rps[opp] % 3) + 1 == rps[you]:
        # We want to catch the roll over from SCISSORS losing to ROCK
        # Modulus 3 means that the opponent picking SCISSORS rolls over to
        # 0. Adding 1 to account for this being a 1-indexed score list.
        # If you picked ROCK, those numbers match and you win!
        score += WIN + rps[you]
    else:
        score += LOSE + rps[you]

    if score == 0:
        # ABC
        print("Some logic error happened when we got {} {}".format(opp, you))
        sys.exit(1)

    return score


def playRPS(rpsList):
    totalScore = 0

    for line in rpsList:
        opp, you = line.split()
        totalScore += scoreRPS(opp, you)

    return totalScore


def fixRPS(rpsList):
    totalScore = 0
    oppMoves = ['A', 'B', 'C']
    yourMoves = ['X', 'Y', 'Z']

    for line in rpsList:
        opp, you = line.split()
        curIndex = oppMoves.index(opp)

        if you == 'X':
            # Pick a loser
            loseIndex = (curIndex - 1) % 3
            you = yourMoves[loseIndex]
        elif you == 'Y':
            # Pick a draw
            you = yourMoves[curIndex]
        else:
            # Pick a winrar
            winIndex = (curIndex + 1) % 3
            you = yourMoves[winIndex]

        totalScore += scoreRPS(opp, you)

    return totalScore


if __name__ == "__main__":
    print("Please use the main.py script instead of this one directly")
