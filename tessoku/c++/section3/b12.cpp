#include <bits/stdc++.h>

using namespace std;

long double func(long double x) {
    return pow(x, 3) + x;
}

int main() {

    int N;

    cin >> N;

    long double left = 0;
    long double right = pow(N, 1.0/3.0); // x^3 + x = N なので，x<=N^(1/3)で探索する

    long double mid;

    while (left <= right) {

        mid = (left + right) / 2;

        long double output = func(mid);

        if (output < N) {
            // left = mid + 0.000001;
            left = mid;
        }
        // 許容誤差：0.0001
        else if (abs(output - N) < 0.001) {
            cout << mid << endl;

            // デバッグ
            // cout << output << endl;

            return 0;
        }
        else {
            // right = mid - 0.000001;
            right = mid;
        }

    }

}

