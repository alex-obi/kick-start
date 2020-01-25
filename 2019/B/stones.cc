#include <bits/stdc++.h>

using namespace std;

int T;
int N;
int S[100];
int E[100];
int L[100];
int P[100];

bool swap(int i, int j) {
  return L[i] * S[j] < L[j] * S[i];
}

void init_p() {
  for(int i=0; i < N; i++) {
    P[i] = i;
  }
}

void sort() {
  for(int n=0; n < N-1; n++) {
    for(int k=0; k < N-n-1; k++) {
      if(swap(P[k], P[k+1])) {
        int i = P[k];
        P[k] = P[k+1];
        P[k+1] = i;
      }
    }
  }
}

int max_energy(int time, int i) {
  if(i >= N) {
    return 0;
  }
  int j = P[i];
  int en = max(0, E[j] - L[j] * time);
  int en1;
  if(en > 0) {
    en1 = max_energy(time + S[j], i + 1) + en;
  } else {
    en1 = 0;
  }
  int en2 = max_energy(time, i + 1);
  return max(en1, en2);

}

int main() {
  scanf("%d\n", &T);
  for(int t = 1; t <= T; t++) {
    scanf("%d", &N);
    for(int n = 0; n < N; n++) {
      scanf("%d%d%d", &S[n], &E[n], &L[n]);
    }
    init_p();
    sort();
    int e = max_energy(0, 0);
    printf("Case #%d: %d\n", t, e);
  }
}
