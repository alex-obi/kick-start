#include <bits/stdc++.h>

using namespace std;

int T, N;
int S[100], E[100], L[100], P[100];
int cache[10000][100];

bool cmp(int i, int j) {
  return L[i] * S[j] > L[j] * S[i];
}

void init_p(int n) {
  for(int i=0; i < n; i++) {
    P[i] = i;
  }
}

int max_energy(int time, int i) {
  if(i >= N) return 0;
  if(cache[time][i] != -1) return cache[time][i];
  int j = P[i];
  int en_diff = E[j] - L[j] * time;
  int en = max(0, en_diff);
  int en1 = max_energy(time + S[j], i + 1) + en;
  int en2 = max_energy(time, i + 1);
  return cache[time][i] = max(en1, en2);
}

int main() {
  scanf("%d\n", &T);
  for(int t = 1; t <= T; t++) {
    scanf("%d", &N);
    for(int n = 0; n < N; n++) {
      scanf("%d%d%d", &S[n], &E[n], &L[n]);
    }
    init_p(N);
    memset(cache, -1, sizeof cache);
    sort(P, P + N, cmp);
    int e = max_energy(0, 0);
    printf("Case #%d: %d\n", t, e);
  }
}
