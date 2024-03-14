#include <bits/stdc++.h>

using namespace std;

int N, Q;
int X[100009], Y[100009], SUM[1509][1509];
int As[100009], Bs[100009], Cs[100009], Ds[100009];

int array_for_points[1509][1509];

int H, W;


int main() {

	cin >> N;

	for (int i = 1; i <= N; i++) cin >> X[i] >> Y[i];

	cin >> Q;

	for (int i = 1; i <= Q; i++) cin >> As[i] >> Bs[i] >> Cs[i] >> Ds[i];
	
	// 計算量を減らすために，1500ではなく，X, Yの最大値を使う
	H = *max_element(X, X + N);
	W = *max_element(Y, Y + N);

	// 初期化
	for (int i = 0; i <= H; i++) {
		for (int j = 0; j <= W; j++) {
			SUM[i][j] = 0;
			array_for_points[i][j] = 0;
		}
	}

	// 行列の座標を記録
	for (int i = 1; i <= N; i++){
		// array_for_points[X[i]][Y[i]] = 1; // これだと，同じ座標が複数ある場合に対応できない
		array_for_points[X[i]][Y[i]]++;
	}

	// 行方向に和を計算
	for (int i = 1; i <= H; i++) {
		for (int j = 1; j <= W; j++){
			SUM[i][j] = SUM[i][j - 1] + array_for_points[i][j];
		}
	}

	// 列方向に和を計算
	for (int j = 1; j <= W; j++) {
		for (int i = 1; i <= H; i++){
			 SUM[i][j] = SUM[i - 1][j] + SUM[i][j];
		}
	}

	for (int i = 1; i <= Q; i++) {
		cout << SUM[Cs[i]][Ds[i]] + SUM[As[i] - 1][Bs[i] - 1] - SUM[As[i] - 1][Ds[i]] - SUM[Cs[i]][Bs[i] - 1] << endl;
	}

}
