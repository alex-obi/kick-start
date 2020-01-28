import numpy as np


def sort():
    rating = -L / S
    return np.argsort(rating)

def max_energy(time, i):
    if i >= N: return 0
    if Cache[time][i] != -1: return Cache[time, i];
    j = P[i]
    en_rem = E[j] - L[j] * time # remaining power at t=time
    en = max(0, en_rem) # powerup
    en1 = max_energy(time + S[j], i + 1) + en
    en2 = max_energy(time, i + 1)
    c =  max(en1, en2)
    Cache[time, i] = c
    return c

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    S = np.empty(N, np.int_)
    E = np.empty(N, np.int_)
    L = np.empty(N, np.int_)
    Cache = np.full((100 * N, N), -1)
    for n in range(N):
        S[n], E[n], L[n] = map(int, input().split())
    P = sort()
    e = max_energy(0, 0)
    print("Case #{}: {}".format(t, e))
