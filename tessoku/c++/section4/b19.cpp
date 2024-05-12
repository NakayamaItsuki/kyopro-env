#include <bits/stdc++.h>

using namespace std;

long long N, W, w_s[109], v_s[109];
long long dp[109][100009]; // 商品の数 * 価値の配列，重さを格納する．A19は商品の数 * 重さの配列で，価値を格納していた．

int main() {
	// 入力・配列の初期化
	cin >> N >> W;
	for (int i = 1; i <= N; i++){
		cin >> w_s[i] >> v_s[i];
	}
	for (int i = 0; i <= N; i++) {
		for (int j = 0; j <= 100000; j++){
			dp[i][j] = 1'000'000'000'000'000LL; // 十分に大きな値で，重さを初期化する．
		}
	}

	// 動的計画法
	dp[0][0] = 0;
	for (int i = 1; i <= N; i++) {

		// 考慮すべき価値は，最大商品数100 * 最大価値1000 = 100000まででOK
		for (int j = 0; j <= 100000; j++) {
			
			// 価値がjより小さい場合は，dp[i][j] = dp[i - 1][j]とする
			if (j < v_s[i]){
				dp[i][j] = dp[i - 1][j];
			}

			// dp[i - 1][j]は，i番目の商品を選ばない場合の重さ
			// dp[i - 1][j - v_s[i]] + w_s[i]は，i番目の商品を選ぶ場合の重さ
			// 重さは小さい方が良いので，minを取っている
			// メモ：A19は，価値を格納していたので，maxを取っていた．
			else{
				dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - v_s[i]] + w_s[i]);
			}

		}
	}

	// 答えの出力
	long long Answer = 0;
	for (int i = 0; i <= 100000; i++) {
		// 重さがWを超える可能性があるので，dp[N][i] <= Wとして，最大の価値を探す
		if (dp[N][i] <= W) Answer = i;
	}

	cout << Answer << endl;
}
