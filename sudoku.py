#  Title: Sudoku Checker
#  Purpose: Check to see if any given sudoku grid is correct
#  Author: Axel-Jose Persinger

from sympy import *

def isProperSudoku(matrix):
    for i in xrange(9):
        rowSum = 0
        colSum = 0
        for number in matrix.row(i):
            rowSum += number

        for number in matrix.col(i):
            colSum += number

        if colSum != 36 and rowSum != 36:
            return false

    return true

# -------------------------------------------------------------------------- #
#  Program:
#    1. Read in a sudoku puzzle from the file
#    2. Check if any Eigenvalues are 36, if so check if the vector are all 1's
#    3. Repeat process with the Transpose
# -------------------------------------------------------------------------- #
print "Welcome to the Sudoku Solver!"

# Read in the puzzle strings from the file
puzzleTxt = open('puzzles.txt', 'r')
puzzleTxt = puzzleTxt.readlines()

# Ignore everything between the two ':'
puzzles = [item[item.index(":") + 1:item.index(":", item.index(":")+1)] for item in puzzleTxt]

# Create list comprehension to get a list of straight digits
listOfDigs = [char for item in puzzles for char in item]
gridSpace = []
numberPuzzles = len(puzzles)

# Create the list of matrices
t = 0
for k in xrange(numberPuzzles):
    gridSpace.append(eye(9))
    for i in xrange(81):
        (gridSpace[k])[int(i/9),i%9] = int(listOfDigs[t])
        t += 1

for puzzle in gridSpace:
    print isProperSudoku(puzzle)
