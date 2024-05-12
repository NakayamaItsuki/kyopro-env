#include <bits/stdc++.h>

using namespace std;


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

    int dp[100009];

    // スタート地点
    dp[1] = 0;

    // 2番目の地点
    dp[2] = dp[1] + As[2];

    // メイン部分
    for (int i=3; i<=N; i++){
        
        int from_i_1 = dp[i-1] + As[i];
        int from_i_2 = dp[i-2] + Bs[i];

        dp[i] = min(from_i_1, from_i_2);

    }

    cout << dp[N] << endl;

}

