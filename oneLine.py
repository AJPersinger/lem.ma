#  Title: Sudoku Checker
#  Purpose: Check to see if any given sudoku grid is correct
#  Author: Axel-Jose Persinger

from sympy import *
import math

def isProperSudoku(matrix):
    return all(b == [x for x in xrange(1, matrix.shape[0]+1)] for b in [sorted(matrix.extract(range(i*int(math.sqrt(matrix.shape[0])), (i+1)*int(math.sqrt(matrix.shape[0]))), range(k*int(math.sqrt(matrix.shape[0])), (k+1)*int(math.sqrt(matrix.shape[0]))))) for k in xrange(int(math.sqrt(matrix.shape[0]))) for i in xrange(int(math.sqrt(matrix.shape[0])))]) and [sorted(matrix.row(i)) for i in xrange(matrix.shape[0])] == [sorted(matrix.col(i)) for i in xrange(matrix.shape[0])] and sorted(matrix.row(0)) == [x for x in xrange(1, matrix.shape[0]+1)]
