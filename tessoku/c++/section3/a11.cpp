#include <bits/stdc++.h>

using namespace std;


int main() {

    int N, X;

    int As[100009];

    cin >> N >> X;

    for (int i = 1; i <= N; i++) {
        cin >> As[i];
    }

    int left = 1;
    int right = N;
    int mid;

    // 二分探索
    while (left <= right) {
        mid = (left + right) / 2;

        if (X < As[mid]) {
            right = mid-1;
        }
        else if (X == As[mid]) {
            cout << mid << endl; // この問題では必ず探索要素が配列に含まれている
            return 0;
        }
        else {
            left = mid+1;
        }
    }

}

