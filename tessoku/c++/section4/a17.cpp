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
    int P[100009]; // P[i]に1つ前の地点を記録する，解答は復元を活用している

    // スタート地点
    dp[1] = 0;
    P[1] = 1;

    // 2番目の地点
    dp[2] = dp[1] + As[2];
    P[2] = 1;

    // メイン部分
    for (int i=3; i<=N; i++){
        
        int from_i_1 = dp[i-1] + As[i];
        int from_i_2 = dp[i-2] + Bs[i];

        // dp[i] = min(from_i_1, from_i_2);

        // i-1からジャンプ
        if (from_i_1 <= from_i_2){
            dp[i] = from_i_1;
            P[i] = i-1;
        }
        else{
            dp[i] = from_i_2;
            P[i] = i-2;
        }

    }

    // 最短コストを出力
    // cout << dp[N] << endl;

    // 最短経路を計算
    int i = N;
    vector<int> route;

    while (true){
        route.push_back(i);
        i = P[i];

        if (i == 1){
            route.push_back(1);
            break;
        }
    }

    // 経路数を出力
    cout << route.size() << endl;

    // 最短経路を出力
    for (int i=route.size()-1; i>=0; i--){
        cout << route[i] << " ";
    }

}

