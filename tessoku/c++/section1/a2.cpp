#include <bits/stdc++.h>

using namespace std;

int main() {
    int N, X, A;

    cin >> N >> X;

    vector<int> input(N);

    for (int i = 0; i < N; i++) {
        cin >> A;
        if (A==X) {
            cout << "Yes" << endl;
            return 0;
        }
    }

    cout << "No" << endl;

}
