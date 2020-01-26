import numpy as np

#
# FUNCTIONS
#

def result():
    return 0

#
# INPUT
#

# Read number of test cases
T = int(input())

for t in range(1, T + 1):
    # Read variables
    ################

    # Single input
    N = int(input())

    # Double input
    A, B = map(int, input().split())

    # Variable length list
    L = list(map(int, input().split()))

    # Fixed length list
    C = np.fromstring(input(), dtype=int, sep=' ')

    # Multi row double input
    D = np.empty(N, np.int_)
    E = np.empty(N, np.int_)
    for n in range(N):
        D[n], E[n] = map(int, input().split())

    # Matrix input
    M = np.empty((A, B), np.int_)
    for a in range(A):
        E[a] = np.fromstring(input(), dtype=int, sep=' ')

    # Calc output
    #############
    e = result()

    # Print result
    ##############
    print("Case #{}: {}".format(t, e))
