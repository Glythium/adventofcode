#!/usr/bin/python3


import argparse


import prep


def usage():
    print("./main.py -d <DAY>")


def main():
    solutions = {
        "0": usage,
        "1": prep.solveDay01,
        "2": prep.solveDay02
    }

    parser = argparse.ArgumentParser(description='Advent of Code 2022 solver!')
    parser.add_argument('-d', '--day',
                        type=int,
                        default=0,
                        help='The day you want the solution for. Example: -d <1|10|31>')

    args = parser.parse_args()
    
    try:
        day = str(args.day)
        answer = solutions[day]()
        if answer is not None:
            print("Day {}: {}".format(day, answer))
    except KeyError:
        print("That day has not been solved!")


if __name__ == '__main__':
    main()