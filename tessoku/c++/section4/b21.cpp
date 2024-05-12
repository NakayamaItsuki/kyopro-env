#include <bits/stdc++.h>

using namespace std;


// 解答を参考に作成

int dp[1009][1009];
// dp[l][r] := l文字目からr文字目までの部分における最長回文の長さ
// 左右に広げていく
// 初期値はdp[i][i] = 1，隣り合う時はdp[i][i+1] = 2

int main() {

    int N;

    string S;

    cin >> N >> S;

    // 初期値，r-l=0,1の場合を埋める
    for (int i = 1; i <= N; i++) {
        dp[i][i] = 1;

        if (i<=N-1) {
            if (S[i-1]==S[i]) {
                dp[i][i+1] = 2;
            } else {
                dp[i][i+1] = 1;
            }
        }
    }


    // dpを斜めに埋めていく！！，具体的にはr-l=2, 3, 4, ..., N-1
    for (int length = 2; length <= N-1; length++) { 
        for (int l = 1; l <= N-length; l++) { // l=1, 2, ..., N-length
            int r = l + length; 

            // l文字目とr文字目が同じ場合は，左と結合するか，右と結合するか，両方結合するか
            if (S[l-1]==S[r-1]) {
                dp[l][r] = max({dp[l][r-1], dp[l+1][r], dp[l+1][r-1]+2});
            }
            
            // そうでない場合は，左と結合するか，右と結合するか
            else {
                dp[l][r] = max(dp[l+1][r], dp[l][r-1]);
            }

        }
    }


    cout << dp[1][N] << endl;

}




/* 
// 区間dp
int dp[1009][1009]; 
// dp[l][r] := l文字目からr文字目までの部分における最長回文の長さ
// 初期値：dp[1][[1] = 0, dp[2][2] = 0, ..., dp[N][N] = 0
// 答え：dp[1][N]

// Sがprogrammingの場合，ng，in，ig，のようにdpの右下から埋めていく．

int main() {

    int N;

    string S;

    cin >> N >> S;

    // 初期値
    for (int i = 1; i <= N; i++) {
        // dp[i][i] = 0;
        dp[i][i] = 1;
    }

    for (int l = N-1; l >= 1; l--) {
        // for (int r = N; l+1<=r; r--) {
        for (int r = l+1; r<=N; r++) {

                // int concat_left, concat_right;

                // // 左と連結する場合，dp[l-1][r]
                // if (S[l-1]==S[r]){
                //     concat_left = dp[l-1][r] + 2;
                // } else { 
                //     concat_left = dp[l-1][r];
                // }

                // // 右と連結する場合
                // if (S[l-1]==S[r-1]){
                //     concat_right = dp[l][r+1] + 2;
                // } else {
                //     concat_right = dp[l][r+1];
                // }

                dp[l][r] = max(dp[l][r-1], dp[l+1][r]);

                // もし，S[l-1]==S[r]で，
                if (S[l-1]==S[r-1]){
                    // dp[l][r] += 2;

                    // 間に文字が入らない場合は2を足す
                    if (l+1==r){
                        dp[l][r] += 2;
                    } 
                    // 間に文字が入る場合は3を足す
                    else {
                        dp[l][r] += 3;
                    }
                }
        }
    }

    cout << dp[1][N] << endl;

}
*/

