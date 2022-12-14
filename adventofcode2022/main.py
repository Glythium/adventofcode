#!/usr/bin/python3


import argparse


from lib.prep import solveDay01
from lib.prep import solveDay02
from lib.prep import solveDay03
from lib.prep import solveDay04
from lib.prep import solveDay05
from lib.prep import solveDay06


def usage():
    print("./main.py -d <DAY>")


def main():
    solutions = {
        "0": usage,
        "1": solveDay01,
        "2": solveDay02,
        "3": solveDay03,
        "4": solveDay04,
        "5": solveDay05,
        "6": solveDay06
    }

    parser = argparse.ArgumentParser(description='Advent of Code 2022 solver!')
    parser.add_argument('-d', '--day',
                        type=int,
                        default=0,
                        help='The day you want the solution for. Example: -d <1|10|31>')

    args = parser.parse_args()

    day = str(args.day)
    if day not in solutions:
        print(f"That day ({day}) has not been solved!")
    else:
        answer = solutions[day]()
        if answer is not None:
            print(f"Day {day}: {answer}")

if __name__ == '__main__':
    main()
