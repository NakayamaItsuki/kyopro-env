#include <bits/stdc++.h>

using namespace std;


// Sとgood_string間のコストを計算する関数
long long calculateCost(const string& S, long long good_string, const vector<int>& C, int N) {
    long long xorValue = stoll(S, nullptr, 2) ^ good_string;
    long long cost = 0;
    for (int i = 0; i < N; ++i) {
        if (xorValue & (1LL << i)) {
            cost += C[i];
        }
    }
    return cost;
}

// すべての良い文字列を生成する関数
void generateGoodStrings(int N, const string& s, vector<long long>& goodStrings) {
    if (s.size() == N) {
        if (countAdjacent(s)) {
            goodStrings.push_back(stoll(s, nullptr, 2));
        }
        return;
    }
    generateGoodStrings(N, s + '0', goodStrings);
    generateGoodStrings(N, s + '1', goodStrings);
}

// 連続する同じ文字が1つだけあるかどうかを確認する関数
bool countAdjacent(const string& s) {
    int count = 0;
    for (size_t i = 0; i < s.size() - 1; ++i) {
        if (s[i] == s[i + 1]) {
            count++;
        }
    }
    return count == 1;
}

int main() {
    int N;
    cin >> N;

    string S;
    cin >> S;

    vector<int> C(N);
    for (int i = 0; i < N; ++i) {
        cin >> C[i];
    }

    // コスト配列を反転させる
    reverse(C.begin(), C.end());

    vector<long long> goodStrings;
    generateGoodStrings(N, "", goodStrings);

    long long minCost = LLONG_MAX;

    for (long long goodString : goodStrings) {
        minCost = min(minCost, calculateCost(S, goodString, C, N));
    }

    cout << minCost << endl;

    return 0;
}
