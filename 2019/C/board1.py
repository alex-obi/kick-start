import numpy as np

#
# FUNCTIONS
#

# Calc row wise number of consecutive cells having same value
def calc_contig():
    P = np.ones((R, C), dtype=int)
    P[:, -1] = 1
    for r in range(R):
        for c in range(1, C):
            if V[r, C - c] == V[r, C - 1 - c]:
                P[r, C -1 - c] += P[r, C - c]
    return P

# Give biggest rect if x is interpreted as a histogram
def max_rect_hist(x):
    stack = [-1]
    max_rect = 0
    # Build stack, pop if descending
    for i in range(len(x)):
        while(len(stack) > 1 and x[stack[-1]] >= x[i]):
            ix = stack.pop()
            length = (i - 1) - stack[-1]
            max_rect = max(max_rect, x[ix] * length)
        stack.append(i)
    # Check remaining elements
    while(len(stack) > 1):
        ix = stack.pop()
        length = (len(x) - 1) - stack[-1]
        max_rect = max(max_rect, x[ix] * length)
    return max_rect

# Calc column wise max rect
def max_rect():
    best_max = 0
    for c in range(C):
        new_max = max_rect_hist(P[:, c])
        best_max = max(new_max, best_max)
    return best_max


#
# INPUT
#

# Read number of test cases
T = int(input())

for t in range(1, T + 1):
    # Read variables
    ################
    R, C, K = map(int, input().split())

    V = np.empty((R, C), np.int_)
    for r in range(R):
        V[r] = np.fromstring(input(), dtype=int, sep=' ')

    # Calc output
    #############
    P = calc_contig()
    result = max_rect()

    # Print result
    ##############
    print("Case #{}: {}".format(t, result))
