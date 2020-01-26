#include <bits/stdc++.h>

using namespace std;

const int N_max = 1e5;
int T;
int N;
int S;
int A[N_max];
int counts[N_max];
int scores[N_max];

void init_counts() {
  for(int i = 0; i < N_max; i++) {
    counts[i] = 0;
  }
}

void comp_scores(int l) {
  int a, c;
  for(int i=0; i < N - l; i++){
    a = A[i + l];
    c = counts[a];
    counts[a] += 1;
    if(c < S) {
      scores[i] = 1;
    }
    if(c > S) {
      scores[i] = 0;
    }
    if(c == S) {
      scores[i] = -S;
    }
  }
}

int max_score(int l) {
  init_counts();
  comp_scores(l);

  int e = 0;
  int sum = 0;
  for(int i = 0; i < N - l; i++) {
    sum += scores[i];
    if(sum > e) {
      e = sum;
    }
  }
  return e;
}

int main() {
  scanf("%d\n", &T);
  for(int t = 1; t <= T; t++) {
    scanf("%d%d", &N, &S);
    for(int n = 0; n < N; n++) {
      scanf("%d", &A[n]);
    }
    int e = 0;
    for(int l = 0; l < N; l++) {
      e = max(max_score(l), e);
    }
    printf("Case #%d: %d\n", t, e);
  }
}
