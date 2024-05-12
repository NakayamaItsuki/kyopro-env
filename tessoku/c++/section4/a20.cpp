#include <bits/stdc++.h>

using namespace std;

int dp[2009][2009]; // dp[i][j] := マス(i,j)に到達するまでに通る，赤い辺の本数の最大値

int main() {

    string S, T;

    cin >> S >> T;


    // 初期値
    for (size_t i = 0; i < S.size(); i++) {
        dp[i][0] = 0;
    }
    
    for (size_t j = 0; j < T.size(); j++) {
        dp[0][j] = 0;
    }

    // dp
    for (size_t i = 1; i <= S.size(); i++) {
        for (size_t  j = 1; j <= T.size(); j++) {
            
            // Sのi文字目とTのj文字目が一致する場合
            if (S[i-1]==T[j-1]){ // インデックスに注意
                
                // 左，上から移動する場合と，左上から赤い辺で移動する場合がある．
                dp[i][j] = max(max(dp[i-1][j], dp[i][j-1]), dp[i-1][j-1]+1);

            }

            // Sのi文字目とTのj文字目が一致しない場合
            else {

                // 左，上から移動する場合がある．
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]);

            }

        }
    }

    cout<< dp[S.size()][T.size()] <<endl;

}
