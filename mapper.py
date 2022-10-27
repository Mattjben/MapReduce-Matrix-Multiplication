#!/usr/bin/env python3
import sys

# Get matrix size inputs 
M=sys.argv[1].strip().split(',')
N=sys.argv[2].strip().split(',')
X=sys.argv[3].strip().split(',')



# Get the rows and columns from the input arguments of each matrix 
M_row=int(M[0])
M_col=int(M[1])
N_row=int(N[0])
N_col=int(N[1])
X_row=int(X[0])
X_col=int(X[1])


args = sys.stdin.readlines()
for line in args:
    Values = line.strip().split(',')
    

    Matrix_no = Values[0]
    Row_no = Values[1]
    row_vals = Values[2:]
    try:
        Matrix_no=int(Matrix_no)
        Row_no=int(Row_no)
    except:
        # int was not a number, so silently
        # ignore/discard this line
        break
    
    # For each mij and njk value in M and N output:
    # KEY = (i,k)
    # Value = (M,j,mij) or (N,j,njk)
    # this allows us to find SUM(mij * njk) for all values with the same (i,k) pair in the reducer 
    if Matrix_no == 1: # loop for matrix M 
        for j in range(0,M_col):
            for k in range(0,N_col):
                print('%s\t%s\t%s\t%s\t%s' % (Row_no, k,j, Matrix_no,row_vals[j]))

    if Matrix_no == 2: # loop for matrix N
        for k in range(0,N_col):
            for i in range(0,M_row):
                print('%s\t%s\t%s\t%s\t%s' % (i, k, Row_no,Matrix_no,row_vals[k]))

    # For each row and col number output the value of matrix X so it can be subtracted from the sum calculated using M and N  
    if Matrix_no == 3: # loop for matrix X
        for i in range(0,X_col):
                print('%s\t%s\t%s\t%s\t%s' % (Row_no,i,M_row+1, Matrix_no,row_vals[i]))
