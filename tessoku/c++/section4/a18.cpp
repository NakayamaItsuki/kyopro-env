#include <bits/stdc++.h>

using namespace std;


int main() {

    int N, S;
    int As[100009];

    cin >> N >> S;

    for (int i = 1; i <= N; i++) {
        cin >> As[i];
    }

    bool dp[69][10009]; // N * S の配列を格納する

    // メモ：dp[i][j] は、i番目までの整数を使って、総和がjになるような組み合わせが存在するかどうかを表す

    // 初期化，カードが0枚の場合
    dp[0][0] = true;
    for (int j = 1; j <= S; j++) {
        dp[0][j] = false;
    }

    // メイン部分
    for (int i=1; i<=N; i++){
        for (int j=0; j<=S; j++){

            // i-1番目まででjが作れる時
            if (dp[i-1][j] == true){
                dp[i][j] = true;
            }

            // // i-1番目まででj-As[i]が作れる時
            // else if (dp[i-1][j-As[i]]){
            //     dp[i][j] = true;
            // }

            // i-1番目まででj-As[i]が作れる時，j-As[i]が負の時を考慮する
            else if ((j >= As[i]) && (dp[i-1][j-As[i]])){
                dp[i][j] = true;
            }

            else {
                dp[i][j] = false;
            }
        }
    }


    if (dp[N][S]==true){
        cout << "Yes" << endl;
    }

    else {
        cout << "No" << endl;
    }

}

