#!/usr/bin/python3

class Submarine():
    def __init__(self):
        self.distance = 0
        self.depth = 0
        self.aim = 0
        self.moveSub = {"forward": self.moveForward,
                        "backward": self.moveBackward,
                        "up": self.moveUp,
                        "down": self.moveDown}
        self.gammaRate = 0
        self.epsilonRate = 0
    
    def moveForward(self, x):
        self.distance += x
        self.depth += self.aim * x
    
    def moveBackward(self, x):
        self.distance -= x
    
    def moveUp(self, y):
        self.aim -= y

    def moveDown(self, y):
        self.aim += y
    
    def getPowerConsumption(self):
        return self.gammaRate * self.epsilonRate