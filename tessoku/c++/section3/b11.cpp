#include <bits/stdc++.h>

using namespace std;

int As[100009];


int main() {

    int N, Q;

    int Xs[100009];

    cin >> N;

    for (int i = 1; i <= N; i++) {
        cin >> As[i];
    }

    cin >> Q;

    for (int i = 1; i <= Q; i++) {
        cin >> Xs[i];
    }

    // Asをソートする
    sort(As+1, As+N+1); // 右側は1つオーバーさせる必要あり

    for (int i = 1; i <= Q; i++) {
        // ( lower_bound(As+1, As+N+1, Xs[i]) - As )は，As_i <= X を満たす最大のiの，スタートからの位置を返す
        cout << ( lower_bound(As+1, As+N+1, Xs[i]) - As ) - 1  << endl;
    }

}

