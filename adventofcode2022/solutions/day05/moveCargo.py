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


def makeMoves(cargoDict, cargoInput, moveFunc):
    # Let's find the line separating the cargo from the moves
    lineBreak = cargoInput.index("\n")

    # Now take everything below that line
    for line in cargoInput[lineBreak + 1::]:
        # We just need the numbers here
        numberMoved, sourceColumn, destColumn = line.split()[1::2]
        # Call the function we passed in to move it the desired way
        cargoDict = moveFunc(cargoDict, int(numberMoved), int(sourceColumn), int(destColumn))

    return cargoDict


def restackCargo(cargoDict, numberMoved, sourceColumn, destColumn):
    for i in range(numberMoved):
        buffer = cargoDict[sourceColumn].pop()
        cargoDict[destColumn].append(buffer)

    return cargoDict


def megaRestackCargo(cargoDict, numberMoved, sourceColumn, destColumn):
    # We can grab the whole section to be moved
    # This also keeps it in the correct order
    buffer = cargoDict[sourceColumn][numberMoved * -1::]

    for letter in buffer:
        cargoDict[destColumn].append(letter)
        cargoDict[sourceColumn].pop()

    return cargoDict


def finalCargo(cargoDict):
    letters = ""

    # Build our string using by concatenating the last letter from each list
    for i in cargoDict:
        letters += cargoDict[i][-1]

    return letters


def moveCargo(cargoInput):
    cargoDict = setupCargo(cargoInput)
    cargoDictTwo = setupCargo(cargoInput)
    movedCargoDict = makeMoves(cargoDict, cargoInput, restackCargo)
    movedCargoDictTwo = makeMoves(cargoDictTwo, cargoInput, megaRestackCargo)

    return finalCargo(movedCargoDict), finalCargo(movedCargoDictTwo)


if __name__ == "__main__":
    print("Please use the main.py script instead of this one directly")