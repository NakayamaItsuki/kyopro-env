#include <bits/stdc++.h>

using namespace std;

int main() {

    int N;
    long long K;

    cin >> N >> K;

    long long As[100009];

    for (int i = 1; i <= N; i++) {
        cin >> As[i];
    }

    long long cnt = 0;

    long long R = 1; // 初期値は1 

    long long diff;


    for (int i = 1; i <= N; i++) {
        diff = 0;

        R --; // 最初のR++用に減らしておく

        // diffがKを超えないギリギリまでRを増やす
        while (diff <= K) {
            R ++;
            
            // 最大データ数を超えたらbreak
            if (R > N) {
                break;
            }

            diff =  As[R] - As[i];
        }

        R --; // diffがKを超えたらRを戻す

        cnt += R - i;

    }

    cout << cnt << endl;
    
}


