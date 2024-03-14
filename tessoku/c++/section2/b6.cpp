#include <bits/stdc++.h>

using namespace std;

int main() {
    int N;

    cin >> N;

    int As[N];

    for (int i = 0; i < N; i++) {
        cin >> As[i];
    }

    int Q;

    cin >> Q;

    int Ls[Q], Rs[Q];

    for (int i = 0; i < Q; i++) {
        cin >> Ls[i] >> Rs[i];
    }

    // 累積和
    int cumulative_sums[N+1];

    cumulative_sums[0] = 0; // 0日目の累積和は0

    for (int i = 0; i < N; i++) {
        cumulative_sums[i+1] = cumulative_sums[i] + As[i];
    }

    for (int i = 0; i < Q; i++) {
        int num_atari = cumulative_sums[Rs[i]] - cumulative_sums[Ls[i]-1];
        int num_hazure = ( Rs[i] - Ls[i] + 1 ) - num_atari;

        if (num_atari > num_hazure) {
            cout << "win" << endl;
        } 
        else if (num_atari < num_hazure) {
            cout << "lose" << endl;
        } 
        else {
            cout << "draw" << endl;
        }
    }

}

