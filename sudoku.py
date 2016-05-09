#  Title: Sudoku Checker
#  Purpose: Check to see if any given sudoku grid is correct
#  Author: Axel-Jose Persinger

from sympy import *
import math

def isProperSudoku(matrix):
    oneThruN = [x for x in xrange(1, matrix.shape[0]+1)]

    listOfRows = [sorted(matrix.row(i)) for i in xrange(matrix.shape[0])]
    listOfCols = [sorted(matrix.col(i)) for i in xrange(matrix.shape[0])]

    if listOfRows != listOfCols and matrix.row(0) != oneThruN:
        return False

    n = int(math.sqrt(matrix.shape[0]))
    for i in xrange(n):
        for k in xrange(n):
            if sorted(matrix.extract(range(i*n, (i+1)*n), range(k*n, (k+1)*n))) != oneThruN:
                return False

    return True
