#include <bits/stdc++.h>

using namespace std;

int main() {

    int N, K;

    cin >> N >> K;

    int As[39];

    for (int i = 1; i <= N; i++) {
        cin >> As[i];
    }

    // 2^30は不可能なので，別の手段を試す

    // まずカードを半分に分けて，それぞれのグループで作成可能な和を列挙する

    vector<int> P, Q;

    vector<int> As_left, As_right;

    int half = N / 2;

    for (int i = 1; i <= N; i++) {
        if (i <= half) {
            As_left.push_back(As[i]);
        } else {
            As_right.push_back(As[i]);
        }
    }

    // ビット全探索で和を列挙する
    for (int bit = 0; bit < (1<<As_left.size()); bit++) {
        int sum = 0;
        for (size_t i = 0; i < As_left.size(); i++) { // size_t型で受け取れる
            if (bit & (1<<i)) {
                sum += As_left[i];
            }
        }
        P.push_back(sum);
    }

    for (int bit = 0; bit < (1<<As_right.size()); bit++) {
        int sum = 0;
        for (size_t i = 0; i < As_right.size(); i++) {
            if (bit & (1<<i)) {
                sum += As_right[i];
            }
        }
        Q.push_back(sum);
    }

    // ソート
    sort(Q.begin(), Q.end());


    // 二分探索で和がKになる組み合わせがあるかを調べる
    for (size_t i = 0; i < P.size(); i++) {

        int target = K - P[i];

        size_t pos = lower_bound(Q.begin(), Q.end(), target) - Q.begin();

        if (pos < Q.size() && Q[pos] == target) {
            cout << "Yes" << endl;
            return 0;
        }

    }

    cout << "No" << endl;

}

