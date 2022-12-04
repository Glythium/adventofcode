#!/usr/bin/python3

def isLarger(x, y):
    if y > x:
        return True

def day_1(mySub):
    # Get the input from a manually seeded text file
    with open("input.txt", "r") as fp:
        # Don't parse while the file is open, just grab it
        nums = fp.readlines()

    # This will store our final answer
    increases = 0

    # Go through the input and convert them into integers from strings
    for i in range(len(nums)):
        nums[i] = int(nums[i])
    
    # Find the increases between numbers
    for i in range(len(nums) - 1):
        if isLarger(nums[i], nums[i + 1]):
            increases += 1
    
    # This will display the final answer of the first part
    # of Day 1
    print("There are {} increases".format(increases))

    # Reset the final answer for part 2
    increases = 0

    # Find the increases between the 3-digit windows
    for i in range(len(nums) - 3):
        if isLarger(nums[i] + nums[i + 1] + nums[i + 2],
                    nums[i + 1] + nums[i + 2] + nums[i + 3]):
            increases += 1
        
    print("There are {} increases between the 3-digit windows".format(increases))

if __name__ == "__main__":
    day_1()
