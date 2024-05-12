#include <bits/stdc++.h>

using namespace std;


int main() {

    int N;
    int hs[100009];

    cin >> N;

    int dp[100009];
    
    for (int i = 1; i <= N; i++) {
        cin >> hs[i];
    }

    // スタート地点
    dp[1] = 0;

    // 2つ目の地点
    dp[2] = abs(hs[1]-hs[2]);


    // メイン部分
    for (int i=3; i<=N; i++){
        
        int from_i_1 = dp[i-1] + abs(hs[i-1]-hs[i]);
        int from_i_2 = dp[i-2] + abs(hs[i-2]-hs[i]);

        dp[i] = min(from_i_1, from_i_2);

    }

    cout << dp[N] << endl;

}

