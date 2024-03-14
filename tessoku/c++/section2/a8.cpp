#include <bits/stdc++.h>

using namespace std;

int H, W, Q;
int X[1509][1509], SUM[1509][1509];
int As[100009], Bs[100009], Cs[100009], Ds[100009];


/* これはダメ，メモリの確保は動的にはできない
    int Q;

    cin >> Q;

    int As[Q], Bs[Q], Cs[Q], Ds[Q];
*/


int main() {

	cin >> H >> W;
	for (int i = 1; i <= H; i++) {
		for (int j = 1; j <= W; j++) cin >> X[i][j];
	}
	cin >> Q;
	for (int i = 1; i <= Q; i++) cin >> As[i] >> Bs[i] >> Cs[i] >> Ds[i];

	for (int i = 0; i <= H; i++) {
		for (int j = 0; j <= W; j++) SUM[i][j] = 0;
	}

    // 行方向に和を計算
	for (int i = 1; i <= H; i++) {
		for (int j = 1; j <= W; j++) SUM[i][j] = SUM[i][j - 1] + X[i][j];
	}

	// 列方向に和を計算
	for (int j = 1; j <= W; j++) {
		for (int i = 1; i <= H; i++) SUM[i][j] = SUM[i - 1][j] + SUM[i][j];
	}

	for (int i = 1; i <= Q; i++) {
		cout << SUM[Cs[i]][Ds[i]] + SUM[As[i] - 1][Bs[i] - 1] - SUM[As[i] - 1][Ds[i]] - SUM[Cs[i]][Bs[i] - 1] << endl;
	}

}
