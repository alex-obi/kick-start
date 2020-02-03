import numpy as np
import math

#
# CLASSES
#

class SparseTable():

    def __init__(self, array, query_fun):
        n = len(array)
        self.query_fun = query_fun
        self.mem = np.empty((n, int(math.log2(n)) + 1), dtype=int)
        self.mem[:, 0] = array
        j = 1 # 2**j is size of interval
        while (1 << j) <= n:
            i = 0 # start index of interval
            while (i + (1 << j) - 1) < n:
                self.mem[i, j] = self.query_fun(self.mem[i, j-1], self.mem[i + (1 << (j-1)), j-1])
                i += 1
            j+= 1

    def query(self, l, r):
        j = int(math.log2(r - l + 1))
        return self.query_fun(self.mem[l, j], self.mem[r - (1 << j) + 1, j])

#
# FUNCTIONS
#

# Calc row wise number of consecutive cells where max - min <= K
# C log C runtime
def calc_contig_clogc():
    P = np.empty((R, C), dtype=int)
    for r in range(R):
        st_min =  SparseTable(V[r], min)
        st_max =  SparseTable(V[r], max)
        # binary search for first point x where the
        # interval starting at [c,x] is not valid
        for c in range(C):
            lx = c + 1
            rx = C - 1
            mid = c
            last_valid = True
            while lx <= rx:
                mid = lx + (rx - lx) // 2
                mini = st_min.query(c, mid)
                maxi = st_max.query(c, mid)
                if maxi - mini <= K:
                    lx = mid + 1
                    last_valid = True
                else:
                    rx = mid - 1
                    last_valid = False
            if last_valid:
                P[r, c] = mid - c + 1
            else:
                P[r, c] = mid - c
    return P

# Linear runtime for K=0
def calc_contig_c():
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
    if K == 0:
        P = calc_contig_c()
    else:
        P = calc_contig_clogc()
    result = max_rect()

    # Print result
    ##############
    print("Case #{}: {}".format(t, result))
