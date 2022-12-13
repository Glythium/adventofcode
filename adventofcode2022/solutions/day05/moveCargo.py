#!/usr/bin/python3


def setupCargo(cargoInput):
    cargoDict = dict()

    # Let's find the line separating the cargo from the moves
    lineBreak = cargoInput.index("\n")

    # Now take everything above that line in reverse order
    for idx, line in enumerate(cargoInput[lineBreak - 1::-1]):
        # The first line establishes how many columns there are
        if idx == 0:
            # Create a dictionary with that many columns
            for num in line.split():
                cargoDict[int(num)] = []
        else:
            # Now here come the letters
            # Each letter is 4 spaces apart
            for j, letter in enumerate(line[1::4]):
                # Some spots are just whitespace
                if letter != " ":
                    # Index is offset by 1
                    cargoDict[j + 1].append(letter)
    
    return cargoDict


def restackCargo(cargoDict, numberMoved, sourceColumn, destColumn):
    for i in numberMoved:
        buffer = cargoDict[sourceColumn].pop()
        cargoDict[destColumn].append(buffer)
    
    return cargoDict


def makeMoves(cargoDict, cargoInput):
    # Let's find the line separating the cargo from the moves
    lineBreak = cargoInput.index("\n")

    # Now take everything below that line
    for line in cargoInput[lineBreak + 1::]:
        # We just need the numbers here
        numberMoved, sourceColumn, destColumn = line.split()[1::2]
        cargoDict = restackCargo(cargoDict, numberMoved, sourceColumn, destColumn)
    
    return cargoDict


def finalCargo(cargoDict):
    letters = ""
    for i in len(cargoDict):
        letters += cargoDict[i][-1]
    
    return letters


def moveCargo(cargoInput):
    cargoDict = setupCargo(cargoInput)
    movedCargoDict = makeMoves(cargoDict, cargoInput)

    return finalCargo(movedCargoDict)


if __name__ == "__main__":
    print("Please use the main.py script instead of this one directly")