#  Title: Sudoku Checker
#  Purpose: Check to see if any given sudoku grid is correct
#  Author: Axel-Jose Persinger

from sympy import *
from random import randint

# -------------------------------------------------------------------------- #
#  Gobal Variables:
#    gridSpace - is the matrix representing a sudoku grid
#    gridSpaceT - is the Transpose of gridSpace
#    rowSumEigen - is the eigenvector if a matrix has the rows equalling a sum
#    isSolutionOne - is a boolean to represent the status of a sudoku completion
#    isSolutionTwo - is a boolean to represent the status of a sudoku completion
# -------------------------------------------------------------------------- #
gridSpace = Matrix([
[randint(1,9) for p in range(0,9)],
[randint(1,9) for p in range(0,9)],
[randint(1,9) for p in range(0,9)],
[randint(1,9) for p in range(0,9)],
[randint(1,9) for p in range(0,9)],
[randint(1,9) for p in range(0,9)],
[randint(1,9) for p in range(0,9)],
[randint(1,9) for p in range(0,9)],
[randint(1,9) for p in range(0,9)],
])

gridSpaceT = gridSpace.T

rowSumEigen = Matrix([[1], [1], [1], [1], [1], [1], [1], [1], [1]])

isSolution = false


# -------------------------------------------------------------------------- #
#  Program:
#    1. Generate Eigensystem to gridSpace
#    2. Check if any Eigenvalues are 9, if so check if the vector are all 1's
#    3. Repeat process with the Transpose
# -------------------------------------------------------------------------- #
print "Welcome to the Sudoku Solver!"

# Create Eigensystem for the gridSpace and its transpose
gridSpace_Eigen = gridSpace.eigenvects()
gridSpaceT_Eigen = gridSpaceT.eigenvects()

# Process to check if the sudoku puzzle is solved
for i in xrange(0, len(gridSpace_Eigen)):
        # Check the Eigenvalue to see if it's 9
        if gridSpace_Eigen[i][0] == 9:
            # Check the Eigenvector to see if it's all 1's
            if gridSpace_Eigen[i][3] == rowSumEigen:
                isSolutionOne = true;

# Process to check if the sudoku puzzle is solved
for i in xrange(0, len(gridSpaceT_Eigen)):
        # Check the Eigenvalue to see if it's 9
        if gridSpaceT_Eigen[i][0] == 9:
            # Check the Eigenvector to see if it's all 1's
            if gridSpaceT_Eigen[i][3] == rowSumEigen:
                isSolutionOne = true;


if isSolutionOne == true and isSolutionTwo == true:
    print "The Sudoku puzzle is a correct solution"
else:
    print "Sorry! The puzzle has errors"
