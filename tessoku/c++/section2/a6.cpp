#include <bits/stdc++.h>

using namespace std;

int main() {
    int N, Q;

    cin >> N >> Q;

    int As[N];

    for (int i = 0; i < N; i++) {
        cin >> As[i];
    }

    vector<int> LRs[Q];

    for (int i = 0; i < Q; i++) {
        int L, R;
        cin >> L >> R;
        LRs[i].push_back(L);
        LRs[i].push_back(R);
    }

    // 累積和
    vector<int> cumulative_sums;
    cumulative_sums.push_back(0); // 0日目の累積和は0

    int sum = 0;
    for (int i : As) {
        sum += i;
        cumulative_sums.push_back(sum);
    }

    for (vector<int> LR : LRs){
        cout<< (cumulative_sums[LR[1]] - cumulative_sums[LR[0]-1]) <<endl;
    }

}

