#  Title: Sudoku Checker
#  Purpose: Check to see if any given sudoku grid is correct
#  Author: Axel-Jose Persinger


from sympy import *
from sudoku import isProperSudoku
# -------------------------------------------------------------------------- #
#  Program:
#    1. Read in a sudoku puzzle from the file
#    2. Create a list of sympy matrices
#    2. Check the sum of rows and columns, the elements of the rows and columns,
#           and the length of the rows and columns to ensure they are proper
#    3. Return true or false
# -------------------------------------------------------------------------- #

# For the record, the longest part of this code is reading in the data from the
#      file, not any of the algorthms

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
        (gridSpace[k])[int(i/9),i%9] = int(listOfDigs[t])+1
        t += 1

for i in xrange(numberPuzzles):
    print isProperSudoku(gridSpace[i])
