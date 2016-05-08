#  Title: Sudoku Checker
#  Purpose: Check to see if any given sudoku grid is correct
#  Author: Axel-Jose Persinger

from sympy import *
import math

def isProperSub(matrix):
    n = int(math.sqrt(matrix.shape[0]))
    sortedList = [x for x in xrange(1, matrix.shape[0]+1)]
    rowSlice = [x for x in xrange(n)]
    colSlice = [x for x in xrange(n)]

    for i in xrange(n):
        for k in xrange(n):
            if sorted(matrix.extract(range(i*n, (i+1)*n), range(k*n, (k+1)*n))) != sortedList:
                return False
    return True


def isProperSudoku(matrix):
    sortedList = [x for x in xrange(1, matrix.shape[0]+1)]

    for i in xrange(matrix.shape[0]):
        if sorted(matrix.row(i)) != sortedList \
        or sorted(matrix.col(i)) != sortedList:
            return False

    return isProperSub(matrix)


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

print isProperSudoku(gridSpace[0])
# Test sub matrices and the matrix
#for i in xrange(numberPuzzles):
#    print isProperSudoku(gridSpace[i])
