#include <bits/stdc++.h>

using namespace std;

int N, D;
int As[100009], Ls[100009], Rs[100009];
int Ps[100009], Qs[100009];

int left_max, right_max;


int main() {

	cin >> N;

	for (int i = 1; i <= N; i++){
		cin >> As[i];
	}

	cin >> D;

	for (int i = 1; i <= D; i++){
		cin >> Ls[i] >> Rs[i];
	}

	// Leftからスタートしたmaxを計算
	Ps[1] = As[1];
	for (int i = 2; i <= N; i++) Ps[i] = max(Ps[i - 1], As[i]);

	// Rightからスタートしたmaxを計算
	Qs[N] = As[N];
	for (int i = N - 1; i >= 1; i--) Qs[i] = max(Qs[i + 1], As[i]);

	for (int d = 1; d <= D; d++) {
		cout << max(Ps[Ls[d] - 1], Qs[Rs[d] + 1]) << endl;
	}

}