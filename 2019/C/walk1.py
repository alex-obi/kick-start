import numpy as np

#
# FUNCTIONS
#

def step(r, c, move):
    if move == 'N':
        if world[r-1, c] == 1:
            return step(r-1, c, move)
        else:
            world[r-1, c] = 1
            return r-1, c
    if move == 'E':
        if world[r, c+1] == 1:
            return step(r, c+1, move)
        else:
            world[r, c+1] = 1
            return r, c+1
    if move == 'S':
        if world[r+1, c] == 1:
            return step(r+1, c, move)
        else:
            world[r+1, c] = 1
            return r+1, c
    if move == 'W':
        if world[r, c-1] == 1:
            return step(r, c-1, move)
        else:
            world[r, c-1] = 1
            return r, c-1


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

    world = np.zeros((R, C), dtype=int)
    world[SR-1, SC-1] = 1

    # Calc output
    #############
    er = SR - 1
    ec = SC - 1
    for m in moves:
        er, ec = step(er, ec, m)

    # Print result
    ##############
    print("Case #{}: {} {}".format(t, er+1, ec+1))
