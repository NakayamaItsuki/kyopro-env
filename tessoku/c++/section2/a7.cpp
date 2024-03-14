#include <bits/stdc++.h>

using namespace std;

int main() {
    int D, N;

    cin >> D >> N;

    int Ls[N], Rs[N];

    for (int i = 0; i < N; i++) {
        cin >> Ls[i] >> Rs[i];
    }

    // 前日比を格納する配列
    int compared_to_the_previous_day[D+1]; // 0日目も含めるので+1

    // 0で初期化
    fill(compared_to_the_previous_day, compared_to_the_previous_day + (D+1), 0);

    for (int i = 0; i < N; i++) {
        compared_to_the_previous_day[Ls[i]] += 1; // 参加者が増える
        compared_to_the_previous_day[Rs[i]+1] -= 1; // 参加者が減る
    }

    int num_attendees = 0;
    for (int i = 1; i < D+1; i++) {
        num_attendees += compared_to_the_previous_day[i];
        cout << num_attendees << endl;
    }

}

