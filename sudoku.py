#  Title: Sudoku Checker
#  Purpose: Check to see if any given sudoku grid is correct
#  Author: Axel-Jose Persinger

from sympy import *

def isProperSudoku(matrix):
    sortedList = [x for x in xrange(1, 10)]
    k = sqrt(matrix.shape[0])
    sumRowCol = sum(matrix.row(0))
    if(k % 1 == 0):
        '''
        print matrix
        print matrix[:k, :k]
        print matrix[:k, k:-k]
        print matrix[:k, -k:]
        print matrix[k:-k, :k]
        print matrix[k:-k, k:-k]
        print matrix[k:-k, -k:]
        print matrix[-k:, -k:]
        print matrix[-k:, k:-k]
        print matrix[-k:, :k]
        print isProperSudoku(matrix[:k, :k])
        print isProperSudoku(matrix[:k, k:-k])
        print isProperSudoku(matrix[:k, -k:])
        print isProperSudoku(matrix[k:-k, :k])
        print isProperSudoku(matrix[k:-k, k:-k])
        print isProperSudoku(matrix[k:-k, -k:])
        print isProperSudoku(matrix[-k:, -k:])
        print isProperSudoku(matrix[-k:, k:-k])
        print isProperSudoku(matrix[-k:, :k])
        '''
        if  isProperSudoku(matrix[:k, :k]) == True \
        and isProperSudoku(matrix[:k, k:-k]) == True \
        and isProperSudoku(matrix[:k, -k:]) == True \
        and isProperSudoku(matrix[k:-k, :k]) == True \
        and isProperSudoku(matrix[k:-k, k:-k]) == True \
        and isProperSudoku(matrix[k:-k, -k:]) == True \
        and isProperSudoku(matrix[-k:, -k:]) == True \
        and isProperSudoku(matrix[-k:, k:-k]) == True \
        and isProperSudoku(matrix[-k:, :k]) == True:
            return True
    else:
         if sorted(matrix) == sortedList:
             for i in xrange(matrix.shape[0]):
                if sum(matrix.row(i)) == sumRowCol \
                or sum(matrix.col(i)) == sumRowCol:
                    return True
    return False


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


testMatrixOne = Matrix([
[1, 4, 3, 2],
[2, 1, 4, 3],
[3, 2, 1, 4],
[4, 3, 2, 1]
])

testMatrixTwo = Matrix([
[1, 2, 3, 4, 5, 6, 7, 8, 9],
[9, 1, 2, 3, 4, 5, 6, 7, 8],
[8, 9, 1, 2, 3, 4, 5, 6, 7],
[7, 8, 9, 1, 2, 3, 4, 5, 6],
[6, 7, 8, 9, 1, 2, 3, 4, 5],
[5, 6, 7, 8, 9, 1, 2, 3, 4],
[4, 5, 6, 7, 8, 9, 1, 2, 3],
[3, 4, 5, 6, 7, 8, 9, 1, 2],
[2, 3, 4, 5, 6, 7, 8, 9, 1]
])


# Test sub matrices and the matrix
for i in xrange(numberPuzzles):
    print isProperSudoku(gridSpace[i])


#is for top middle
#is for top right
#is for middle left
#is for middle middle
#is for bottom right
#is for bottom middle
#is for bottom left
