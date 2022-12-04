#!/usr/bin/python3
    

def day_2(mySub):
    # Get the input from a manually seeded text file
    with open("input.txt", "r") as fp:
        # Don't parse while the file is open, just grab it
        lines = fp.readlines()
    
    # Create our list of tuples containing the heading and distance
    directions = []
    for line in lines:
        directions.append(line.split())
    
    # Instantiate a Submarine object to keep track of the distance
    mySub = Submarine()

    # Move the Submarine
    for d in directions:
        # We're going to pull these values into variables for readability
        heading = d[0]
        distance = int(d[1])

        mySub.moveSub[heading](distance)

    print("Final distance is {}".format(mySub.distance * mySub.depth))

if __name__ == "__main__":
    day_2()