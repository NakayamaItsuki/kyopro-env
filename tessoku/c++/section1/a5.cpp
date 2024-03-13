#include <bits/stdc++.h>

using namespace std;

int main() {
    int N, K;

    cin >> N >> K;

    int cnt = 0;

    // for (int i=1; i<N+1; i++) {
    //     for (int j=1; j<N+1; j++) {
    //         for (int k=1; k<N+1; k++) {
    //             if (i+j+k == K) {
    //                 cnt++;
    //             }
    //         }
    //     }
    // }

    // 工夫する
    for (int i=1; i<N+1; i++) {
        for (int j=i; j<N+1; j++) {
            for (int k=j; k<N+1; k++) {
                if (i+j+k == K) {
                    if (i == j && j == k) {
                        cnt++;
                    } else if (i == j || j == k || k == i) {
                        cnt += 3;
                    } else {
                        cnt += 6;
                    }
                }
            }
        }
    }

    cout << cnt << endl;

}