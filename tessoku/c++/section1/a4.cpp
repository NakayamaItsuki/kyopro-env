#include <bits/stdc++.h>

using namespace std;

int main() {
    int N;

    cin >> N;

    int binary[10];

    int i = 0;

    for (int j = 0; j < 10; j++) {
        binary[i] = N % 2;
        N = N / 2;
        i ++;
    }

    for (int j = 10-1; j >= 0; j--) {
        cout << binary[j];
    }

}
