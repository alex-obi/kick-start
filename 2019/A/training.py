def f(N, P, Si):
    Si.sort()
    S_min = sum(Si[P-1] - s for s in Si[:P])
    for i in range(1, N - P + 1):
        S_sum = sum(Si[P + i - 1] - s for s in Si[i:i+P-1])
        if S_sum < S_min:
            S_min = S_sum
    return S_min

T = int(input())

for i in range(1, T + 1):
    N, P = map(int, input().split())
    Si = list(map(int, input().split()))
    print("Case #{}: {}".format(i, f(N, P, Si)))
