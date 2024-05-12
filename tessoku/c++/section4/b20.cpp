#include <bits/stdc++.h>

using namespace std;

int dp[2009][2009]; // dp[i][j] := Sのi文字目までをTのj文字目までに一致させるために必要なコスト

int main() {

    string S, T;

    cin >> S >> T;

    // 編集距離：難しい．
    // SとTから文字列を取り出して，2行に並べる操作を行う．
    // 削除操作：Sの下にTの文字を置かない（Sの文字を削除してTになるように），dp[i-1][j]+1 // Sのi文字目の下に，Tのj文字目を置かない
    // 変更操作：SとTに異なる文字を置く（Sの文字を変更してTになるように），dp[i-1][j-1]+1 // Sのi文字目とTのj文字目に，別の文字を置く．ただし，同じ文字ならコストは追加でかからない．
    // 挿入操作：Tの上にSの文字を置かない（SにTの文字を削除してTになるように），dp[i][j-1]+1 // Tのj文字目の上に，Sのi文字目を置かない．


    // 初期値
    for (size_t i = 0; i <= S.size(); i++) {
        dp[i][0] = i; // i回の挿入操作
    }
    
    for (size_t j = 0; j <= T.size(); j++) {
        dp[0][j] = j; // j回の削除操作
    }

    // dp
    for (size_t i = 1; i <= S.size(); i++) {
        for (size_t  j = 1; j <= T.size(); j++) {

            // 変更操作のコスト
            int change_cost;

            if (S[i-1]==T[j-1]){
                change_cost = 0;
            }

            else {
                change_cost = 1;
            }

            dp[i][j] = min(min(dp[i-1][j]+1, dp[i][j-1]+1), dp[i-1][j-1]+change_cost);

        }
    }

    cout<< dp[S.size()][T.size()] <<endl;

}
