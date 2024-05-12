#include <bits/stdc++.h>

using namespace std;

// 区間dp
int dp[100009]; // dp[i] := マスiまで進んで得られるスコアの最大値


int main() {

    int N;

    int As[100009], Bs[100009];

    cin >> N;

    for (int i = 2; i <= N; i++) {
        cin >> As[i];
    }

    for (int i = 3; i <= N; i++) {
        cin >> Bs[i];
    }

    // 初期値
    dp[1] = 0;
    for (int i = 2; i <= N; i++) {
        dp[i] = 1'000'000'000;
    }

   // 配るDP

    // 問題文を書き換える
    // iからi+1に移動するのに，A_(i+1)分かかる
    // iからi+2に移動するのに，B_(i+2)分かかる

    for (int i = 1; i <= N-1; i++) {

        // i+1に進む場合
        dp[i+1] = min(dp[i+1], dp[i] + As[i+1]);

        if (i <= N-2){
            // i+2に進む場合
            dp[i+2] = min(dp[i+2], dp[i] + Bs[i+2]);
        }

    }

    cout << dp[N] << endl;

}

