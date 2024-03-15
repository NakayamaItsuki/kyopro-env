#include <bits/stdc++.h>

using namespace std;

int main() {

    int N;
    long long K;

    cin >> N >> K;

    long long As[1009], Bs[1009], Cs[1009], Ds[1009];

    int P[1000009], Q[1000009];


    for (int i = 1; i <= N; i++) {
        cin >> As[i];
    }

    for (int i = 1; i <= N; i++) {
        cin >> Bs[i];
    }

    for (int i = 1; i <= N; i++) {
        cin >> Cs[i];
    }

    for (int i = 1; i <= N; i++) {
        cin >> Ds[i];
    }

    /* ステップ1 */

    // 箱Aと箱Bの組み合わせを全て試す
    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= N; j++) {
            P[(i-1)*N + j] = As[i] + Bs[j];
        }
    }

    // 箱Cと箱Dの組み合わせを全て試す
    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= N; j++) {
            Q[(i-1)*N + j]= Cs[i] + Ds[j];
        }
    }
    
    /* ステップ2 */

    //  Qの中にK-P[i]があるかどうかを二分探索で調べる

    // ソート
    sort(Q + 1, Q + N * N + 1);

    bool flag = false;
    
    long long target;

    for (int i=1; i<=N*N; i++){

        // 二分探索
        target = K - P[i];

        if (binary_search(Q + 1, Q+ N * N + 1, target)){
            flag = true;
        }

    }

    if (flag){
        cout << "Yes" << endl;
    }
    else{
        cout << "No" << endl;
    }

    return 0;

}

