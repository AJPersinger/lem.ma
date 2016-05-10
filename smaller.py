#  Title: Sudoku Checker
#  Purpose: Check to see if any given sudoku grid is correct
#  Author: Axel-Jose Persinger

from sympy import *
import math

def isProperSudoku(matrix):
    oneThruN = [x for x in xrange(1, matrix.shape[0]+1)]
    listOfRows = [sorted(matrix.row(i)) for i in xrange(matrix.shape[0])]
    listOfCols = [sorted(matrix.col(i)) for i in xrange(matrix.shape[0])]
    n = int(math.sqrt(matrix.shape[0]))
    cutList = [sorted(matrix.extract(range(i*n, (i+1)*n), range(k*n, (k+1)*n))) for k in xrange(n) for i in xrange(n)]

    return listOfRows == listOfCols and sorted(matrix.row(0)) == oneThruN and all(j == oneThruN for j in cutList)
