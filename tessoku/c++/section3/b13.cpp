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

    long long R = 0; // 初期値は0

    long long sum = 0;

    
    for (int i = 1; i <= N; i++) {

        while (sum <= K){
            R++;
            sum += As[R];
            
            // 最大データ数を超えたらbreak
            if (R > N) {
                break;
            }

        }


        // sumを戻す
        sum -= As[R];
        sum -= As[i];

        // Kを超えたらRを戻す
        R--;
        
        cnt += R - i + 1; // 連続とあるが，1つだけでもOKらしい

    }

    cout << cnt << endl;
    
}

