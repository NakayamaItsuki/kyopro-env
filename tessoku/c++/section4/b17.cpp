#include <bits/stdc++.h>

using namespace std;


int main() {

    int N;
    int hs[100009];

    cin >> N;

    int dp[100009];
    int P[100009];
    
    for (int i = 1; i <= N; i++) {
        cin >> hs[i];
    }

    // スタート地点
    dp[1] = 0;
    P[1] = 0;

    // 2つ目の地点
    dp[2] = abs(hs[1]-hs[2]);
    P[2] = 1;


    // メイン部分
    for (int i=3; i<=N; i++){
        
        int from_i_1 = dp[i-1] + abs(hs[i-1]-hs[i]);
        int from_i_2 = dp[i-2] + abs(hs[i-2]-hs[i]);

        // dp[i] = min(from_i_1, from_i_2);

        if (from_i_1 < from_i_2) {
            dp[i] = from_i_1;
            P[i] = i-1;
        } else {
            dp[i] = from_i_2;
            P[i] = i-2;
        }

    }

    // cout << dp[N] << endl;

    vector<int> route;

    int i = N;

    while (true) {
        route.push_back(i);
        i = P[i];

        if (i == 1) {
            route.push_back(1);
            break;
        }
    }

    // 最短経路の長さを出力
    cout << route.size() << endl;

    // 最短経路を出力
    for (int i = route.size()-1; i >= 0; i--) {
        cout << route[i] << " ";
    }

}

