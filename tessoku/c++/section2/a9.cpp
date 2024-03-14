#include <bits/stdc++.h>

using namespace std;

int H, W, N;
int X[1509][1509], SUM[1509][1509];
int As[100009], Bs[100009], Cs[100009], Ds[100009];


int main() {

	cin >> H >> W >> N;

	for (int i = 1; i <= N; i++){
		cin >> As[i] >> Bs[i] >> Cs[i] >> Ds[i];
	}

	// 初期化
	for (int i = 0; i <= H; i++) {
		for (int j = 0; j <= W; j++) {
			X[i][j] = 0;
			SUM[i][j] = 0;
		}
	}

	for (int i = 1; i <= N; i++){

		// 増やす
		X[As[i]][Bs[i]]++;
		X[Cs[i]+1][Ds[i]+1]++;

		// 減らす
		X[As[i]][Ds[i]+1]--;
		X[Cs[i]+1][Bs[i]]--;
		
	}

	// 行方向に和を計算
		for (int i = 1; i <= H; i++) {
		for (int j = 1; j <= W; j++) SUM[i][j] = SUM[i][j - 1] + X[i][j];
	}

	// 列方向に和を計算
	for (int j = 1; j <= W; j++) {
		for (int i = 1; i <= H; i++) SUM[i][j] = SUM[i - 1][j] + SUM[i][j];
	}

	// SUMを出力
	for (int i = 1; i <= H; i++) {
		for (int j = 1; j <= W; j++){
			cout << SUM[i][j] << " ";
		}
		cout << endl;
	}

}
