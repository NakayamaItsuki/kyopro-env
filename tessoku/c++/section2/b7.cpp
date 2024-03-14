#include <bits/stdc++.h>

using namespace std;

int main() {
    int T, N;

    cin >> T >> N;

    int Ls[N], Rs[N];

    for (int i = 0; i < N; i++) {
        cin >> Ls[i] >> Rs[i];
    }

    // 前日比を格納する配列
    int compared_to_the_previous_time[T+1+1]; // 0日目とT+1日目も含めるので+2

    // 0で初期化
    fill(compared_to_the_previous_time, compared_to_the_previous_time + (T+2), 0);

    for (int i = 0; i < N; i++) {
        compared_to_the_previous_time[Ls[i]] += 1; // 従業員が増える
        compared_to_the_previous_time[Rs[i]] -= 1; // 従業員が減る
    }

    int num_workers = 0;
    for (int i = 0; i < T; i++) {
        num_workers += compared_to_the_previous_time[i];
        cout << num_workers << endl;
    }

}

