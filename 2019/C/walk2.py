import numpy as np

#
# FUNCTIONS
#

# Update the interval dict for row r after visiting column c
def update_row(r, c):
    len1_l = I_R[r].get(c-1, 0)
    len2_r = I_R[r].get(c+1, 0)
    I_R[r][c - len1_l] = len1_l + len2_r + 1
    I_R[r][c + len2_r] = len1_l + len2_r + 1

# Update the interval dict for column c after visiting row r
def update_col(r, c):
    len1_l = I_C[c].get(r-1, 0)
    len2_r = I_C[c].get(r+1, 0)
    I_C[c][r - len1_l] = len1_l + len2_r + 1
    I_C[c][r + len2_r] = len1_l + len2_r + 1

# Perform a step in move direction and update the intervals
def step(r, c, move):
    if move == 'N':
        step = 1 + I_C[c].get(r-1, 0)
        nr, nc = r - step, c
    if move == 'E':
        step = 1 + I_R[r].get(c+1, 0)
        nr, nc =  r, c + step
    if move == 'S':
        step = 1 + I_C[c].get(r+1, 0)
        nr, nc =  r + step, c
    if move == 'W':
        step = 1 + I_R[r].get(c-1, 0)
        nr, nc =  r, c - step
    update_col(r, c)
    update_row(r, c)
    return nr, nc

#
# INPUT
#

# Read number of test cases
T = int(input())

for t in range(1, T + 1):
    # Read variables
    ################
    N, R, C, SR, SC = map(int, input().split())
    moves = input()

    # Use 0,...,N-1 indices
    er = SR - 1
    ec = SC - 1

    # Save blocked intervals for each row and column
    # For each interval save start and end index together with  interval length
    # As dict entries {start: length, end: length}
    I_R = [{} for _ in range(R)]
    I_C = [{} for _ in range(C)]

    # Calc output
    #############
    for m in moves:
        er, ec = step(er, ec, m)

    # Print result
    ##############
    print("Case #{}: {} {}".format(t, er+1, ec+1))
