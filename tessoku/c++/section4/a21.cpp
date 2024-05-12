#include <bits/stdc++.h>

using namespace std;

// 区間dp
int dp[2009][2009]; 
// dp[l][r] := l番目からr番目までのブロックが残っている状況までに，稼ぐことができる最大の点数
// 初めは，dp[1][N]=0，答えはdp[1][1]，dp[2][2]，...，dp[N][N]の最大値

// メモ：模範解答がわかりにくい...

int main() {

    int N;

    int Ps[2009], As[2009];

    cin >> N;

    // // ブロック0を追加
    // As[0] = 0;
    
    // // ブロックN+1を追加
    // As[N+1] = 0;

    for (int i = 1; i <= N; i++) {
        cin >> Ps[i] >> As[i];
    }

    // 初期値
    dp[1][N] = 0;


    // 取り除き方
    // 1. 左端を取り除く．dp[l-1][r]→dp[l][r]...l-1を取り除くので，P[l-1]がまだ残っている（l<=P[l-1]=r)のときに点数ゲット
    // 2. 右端を取り除く．dp[l][r+1]→dp[l][r]...r+1を取り除くので，P[r+1]がまだ残っている（l<=P[r+1]<=r)のときに点数ゲット

    for (int l = 1; l <= N; l++) {
        // for (int r = l; r <= N; r++) {
        for (int r = N; r >= 1; r--) {
            
            int erase_left, erase_right;

            // 左端を取り除いた場合の点数
            if (l<= Ps[l-1] && Ps[l-1] <= r) {
                erase_left = dp[l-1][r] + As[l-1];
            } else {
                erase_left = dp[l-1][r];
            }

            // 右端を取り除いた場合の点数
            if (l<= Ps[r+1] && Ps[r+1] <= r) {
                erase_right = dp[l][r+1] + As[r+1];
            } else {
                erase_right = dp[l][r+1];
            }

            dp[l][r] = max(erase_left, erase_right);

        }
    }

    int max_score = 0;

    for (int i = 1; i <= N; i++) {
        max_score = max(max_score, dp[i][i]);
    }

    cout << max_score << endl;

}
