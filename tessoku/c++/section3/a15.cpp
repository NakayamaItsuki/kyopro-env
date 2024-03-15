#include <bits/stdc++.h>

using namespace std;

int main() {

    int N;
    
    vector<int> As(100009);

    vector<int> Bs(100009);

    vector<int> As_sorted(100009);

    cin >> N;

    for (int i = 1; i <= N; i++) {
        cin >> As[i];
    }

    // コピー
    for (int i = 1; i <= N; i++) {
        As_sorted.push_back(As[i]);
    }

    // ソートする 
    sort(As_sorted.begin(), As_sorted.end());

    // 重複を取り除く
    // uniqueの使い方：https://qiita.com/takuya000885/items/3ead0668127033070b65
    auto result = unique(As_sorted.begin(), As_sorted.end()) - As_sorted.begin(); 
    As_sorted.erase(As_sorted.begin() + result, As_sorted.end());
    
    // 二分探索でAs[i]のインデックスを探す
    for (int i = 1; i <= N; i++) {
        int index = lower_bound(As_sorted.begin(), As_sorted.end(), As[i]) - As_sorted.begin();
        cout << index << ' ';
    }

}

