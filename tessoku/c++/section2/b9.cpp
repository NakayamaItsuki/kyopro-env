#include <bits/stdc++.h>

using namespace std;

int N, H = 1500, W = 1500;
int X[1509][1509], SUM[1509][1509];
int As[100009], Bs[100009], Cs[100009], Ds[100009];


int main() {

	cin >> N;

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

	// 問題用に調整
	for (int i = 1; i <= N; i++){
		Cs[i]--;
		Ds[i]--;
		// As[i]++;
		// Bs[i]++;
	}
	
	for (int i = 1; i <= N; i++){

		// 増やす
		X[As[i]][Bs[i]]++;
		X[Cs[i]+1][Ds[i]+1]++;

		// 減らす
		X[As[i]][Ds[i]+1]--;
		X[Cs[i]+1][Bs[i]]--;
		
	}

	// SUMの端を埋める
	for (int i = 0; i <= H; i++) {
		SUM[i][0] = X[i][0];
	}	
	for (int j = 0; j <= W; j++) {
		SUM[0][j] = X[0][j];
	}
	
	// 行方向に和を計算
	for (int i = 0; i <= H; i++) {
		for (int j = 1; j <= W; j++){
			SUM[i][j] = SUM[i][j - 1] + X[i][j];
		}
	}

	// 列方向に和を計算
	for (int j = 0; j <= W; j++) {
		for (int i = 1; i <= H; i++){
			SUM[i][j] = SUM[i - 1][j] + SUM[i][j];
		}
	}

	int cnt = 0;

	for (int i = 0; i <= H-1; i++) {
		for (int j = 0; j <= W-1; j++){
			if (SUM[i][j] > 0) cnt++;
		}
	}

	cout << cnt << endl;

}
