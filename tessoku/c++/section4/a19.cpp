#include <bits/stdc++.h>

using namespace std;

long long N, W;
long long w_s[109], v_s[109]; // wsはstd::wsと被るので，w_sに変更
long long dp[109][100009];

int main() {

    /* ローカル変数だと，エラーが生じる．chatGPT曰く，グローバル変数にしないと，メモリが足りないらしい． */
    // long long N, W, w[109], v[109];
    // long long dp[109][100009];

	// 入力・配列の初期化
	cin >> N >> W;

	for (int i = 1; i <= N; i++){
        cin >> w_s[i] >> v_s[i];
    }

	for (int i = 0; i <= N; i++) {
		for (int j = 0; j <= W; j++) dp[i][j] = - 1e11;
	}

	// 初期値
	dp[0][0] = 0;

    // メイン部分
	for (int i = 1; i <= N; i++) {
		for (int j = 0; j <= W; j++) {

			if (j < w_s[i]){
                dp[i][j] = dp[i - 1][j];
            }

			else{
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w_s[i]] + v_s[i]);
            }

		}
	}

	// 答えの出力
	long long Answer = 0;

    // 重さがピッタリWの時が，最大の価値を記録しているわけではないので，最大の価値を探す
	for (int i = 0; i <= W; i++){
        Answer = max(Answer, dp[N][i]);   
    }

	cout << Answer << endl;
 
}
