import numpy as np

#
# FUNCTIONS
#

def scores(l):
    counts = {}
    scores = np.empty(N - l, dtype=int)
    for i in range(N - l):
        a = A[i + l]
        c = counts.setdefault(a, 0)
        counts[a] = c + 1
        if c < S:
            scores[i] = 1
        if c > S:
            scores[i] = 0
        if c == S:
            scores[i] = -S
    return scores

def max_score(s):
    e = 0
    sum = 0
    for i in range(len(s)):
        sum += s[i]
        if sum > e:
            e = sum
    return e

#
# INPUT
#

# Read number of test cases
T = int(input())

for t in range(1, T + 1):
    # Read variables
    ################

    N, S = map(int, input().split())
    A = np.fromstring(input(), dtype=int, sep=' ')

    # Calc output
    #############
    e = 0
    for l in range(N):
        s = scores(l)
        e = max(max_score(s), e)

    # Print result
    ##############
    print("Case #{}: {}".format(t, e))
