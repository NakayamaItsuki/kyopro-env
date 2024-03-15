#include <bits/stdc++.h>

using namespace std;

int main() {

    /* 注意：10^9はlong longじゃないと入らない */

    long long N, K;

    long long As[100009];

    cin >> N >> K;

    for (int i = 1; i <= N; i++) {
        cin >> As[i];
    }

    int left = 1;
    long long right = 1000000000;
    long long mid;

    // 二分探索
    while (left <= right) {

        mid = (left + right) / 2;

        // midの時の印刷枚数を計算
        long long X = 0;

        for (int i = 1; i <= N; i++) {
            X += floor(mid / As[i]);
        }

        // デバッグ
        // cout << "left: " << left << " right: " << right << " mid: " << mid << " X: " << X << endl;

        if (X < K) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
 
    }

    cout << left << endl;

}

