#include <bits/stdc++.h>

using namespace std;

// 区間dp
int dp[100009]; // dp[i] := マスiまで進んで得られるスコアの最大値


int main() {

    int N;

    int As[100009], Bs[100009];

    cin >> N;

    for (int i = 1; i <= N-1; i++) {
        cin >> As[i];
    }

    for (int i = 1; i <= N-1; i++) {
        cin >> Bs[i];
    }

    // メモ：2種類のDP
    // 前の状態からdp[i]が決まる...貰うDP
    // dp[i]から次の状態が決まる...配るDP

    // 初期値
    dp[1] = 0;
    for (int i = 2; i <= N; i++) {
        dp[i] = - 1'000'000'000;
    }

    // 配るDP
    for (int i = 1; i <= N-1; i++) {
        
        // A_iに進んだ場合
        dp[As[i]] = max(dp[As[i]], dp[i] + 100);

        // B_iに進んだ場合
        dp[Bs[i]] = max(dp[Bs[i]], dp[i] + 150);
    }

    cout << dp[N] << endl;

}

