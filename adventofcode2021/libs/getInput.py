#!/usr/bin/python3

def getInput(path):
    with open(path, "r") as fp:
        data = fp.readlines()
    return data