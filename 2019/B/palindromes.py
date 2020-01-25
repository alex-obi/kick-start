import numpy as np

def id(char):
    return ord(char) - 65

def build_counts(N, n):
    counts = np.empty((N+1, 26))
    total_count = np.zeros((26))
    counts[0] = total_count
    for i, char in enumerate(n):
        total_count[id(char)] += 1
        counts[i+1] = total_count
    return counts

def check(Li, Ri, counts):
    diff = counts[Ri] - counts[Li-1]
    return np.sum(diff % 2) <= 1

T = int(input())

for t in range(1, T + 1):
    N, Q = map(int, input().split())
    n = input()
    counts = build_counts(N, n)
    c = 0
    for i in range(Q):
        Li, Ri = map(int, input().split())
        c += check(Li, Ri, counts)
    del counts
    print("Case #{}: {}".format(t, c))
