import numpy as np

def swap(i, j):
    return E[j] - min(L[i] * S[j], E[i]) > E[i] - min(L[j] * S[i], E[j])

def sort():
    P = np.arange(N)
    for n in range(N - 1):
        for k in range(N - 1):
            if swap(P[k], P[k+1]): # l < k
                i = P[k]
                P[k] = P[k+1]
                P[k+1] = i
    return P

def max_energy(time, i):
    if i >= N: return 0
    j = P[i]
    en_diff = E[j] - L[j] * time
    en = max(0, en_diff)
    if en > 0:
        # There is still some energy remaining in the stones
        en1 = max_energy(time + S[j], i + 1) + en
    else:
        # All energy is expired
        en1 = 0
    if en_diff < 0:
        # The ordering does not preset a definite choice
        en2 = max_energy(time, i + 1)
    else:
        # The ordering presets the next stone
        en2 = 0
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
