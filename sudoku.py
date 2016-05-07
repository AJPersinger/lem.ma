#  Title: Sudoku Checker
#  Purpose: Check to see if any given sudoku grid is correct
#  Author: Axel-Jose Persinger

from sympy import *

def isProperSudoku(matrix):
    sortedList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    if matrix.shape[0] == 9:
        for i in xrange(matrix.shape[0]):
            if  len(matrix.row(i)) != matrix.shape[0] \
             or len(matrix.col(i)) != matrix.shape[0]\
             or sorted(matrix.row(i)) != sortedList\
             or sorted(matrix.col(i)) != sortedList:
                return False
    else:
        for i in xrange(matrix.shape[0]):
            if  len(matrix.row(i)) != matrix.shape[0] \
             or len(matrix.col(i)) != matrix.shape[0]:
                return False

    return True


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
print isProperSudoku(gridSpace[0][-3:, :3])


for i in xrange(numberPuzzles):
    if isProperSudoku(Matrix(gridSpace[i][:3, :3])) == True \
    and isProperSudoku(gridSpace[i][:3, 3:-3]) == True \
    and isProperSudoku(gridSpace[i][:3, -3:]) == True \
    and isProperSudoku(gridSpace[i][3:-3, :3]) == True \
    and isProperSudoku(gridSpace[i][3:-3, 3:-3]) == True \
    and isProperSudoku(Matrix(gridSpace[i][3:-3 :-3])) == True \
    and isProperSudoku(gridSpace[i][-3:, -3:]) == True \
    and isProperSudoku(gridSpace[i][-3:, 3:-3]) == True \
    and isProperSudoku(gridSpace[i][-3:, :3]) == True \
    and isProperSudoku(gridSpace[i]) == True:
        print True

#is for top middle
#is for top right
#is for middle left
#is for middle middle
#is for bottom right
#is for bottom middle
#is for bottom left
