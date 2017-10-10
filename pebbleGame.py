pebblePileA = 5
pebblePileB = 4


# This is the function the builds the matrix
# TODO it would be better to also do a for loop for pile B
def buildMatrix(sizeA):
    for currentPileA in range(0, sizeA + 1):
        testCaseB = 1
        print(currentPileA, testCaseB)
        if currentPileA + testCaseB % 2 == 0:
            print("Surrender")
        elif (currentPileA % 2 == 0) and (testCaseB % 2 == 1):
            print("take from B")
        elif (currentPileA % 2 == 1) and (testCaseB % 2 == 0):
            print("take from A")
        elif (currentPileA + testCaseB % 2 == 0):
            print("Surrender")
        else:
            print("take from both")


# todo request the value from the keyboard
buildMatrix(6)