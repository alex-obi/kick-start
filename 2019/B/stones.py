import numpy as np

def swap(i, j):
    return L[i] * S[j] < L[j] * S[i]

def sort():
    P = np.arange(N)
    for n in range(N - 1):
        for k in range(N - n - 1):
            if swap(P[k], P[k+1]): # l < k
                i = P[k]
                P[k] = P[k+1]
                P[k+1] = i
    return P

def max_energy(time, i):
    if i >= N: return 0
    j = P[i]
    en = max(0, E[j] - L[j] * time)
    if en > 0:
        en1 = max_energy(time + S[j], i + 1) + en
    else:
        en1 = 0
    en2 = max_energy(time, i + 1)
    return max(en1, en2)

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    S = np.empty(N, np.int_)
    E = np.empty(N, np.int_)
    L = np.empty(N, np.int_)
    for n in range(N):
        S[n], E[n], L[n] = map(int, input().split())
    P = sort()
    e = max_energy(0, 0)
    print("Case #{}: {}".format(t, e))
