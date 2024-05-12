#include <bits/stdc++.h>

using namespace std;


int minCostToGoodString(const string& S, const vector<int>& C) {
    int N = S.size();
    int totalCost = 0;

    for (int i = 0; i < N - 1; ++i) {
        if (S[i] == S[i + 1]) {
            totalCost += min(C[i], C[i + 1]);
            // Make the adjacent pair unique by 'removing' the cheaper change.
            if (C[i] < C[i + 1]) {
                // C[i + 1] = C[i];
            }
        }
    }

    return totalCost;
}

int main() {
    // string S = "0011";
    // vector<int> C = {1, 2, 3, 4};

    int N;
    string S;
    cin >> N >> S;
    vector<int> C(N);
    for (int i = 0; i < N; i++) {
        cin >> C[i];
    }

    int result = minCostToGoodString(S, C);
    cout << "Minimum cost to make the string good: " << result << endl;

    return 0;
}


// int dp[200009][200009];

// int main() {
//     int N;
//     string S;
//     cin >> N >> S;
//     vector<int> C(N);
//     for (int i = 0; i < N; i++) {
//         cin >> C[i];
//     }

//     // dp
    




// }


//     // 良い文字列に変換するための最小コスト
//     int min_cost = INT_MAX;

//     // "良い文字列"の候補を2つ生成 (01 または 10 で交互に繰り返す)
//     string good_string_1, good_string_2;
//     for (int i = 0; i < N; i++) {
//         good_string_1 += (i % 2 == 0) ? '0' : '1';
//         good_string_2 += (i % 2 == 0) ? '1' : '0';
//     }

//     // それぞれの候補に対してコストを計算
//     for (int k = 0; k < 2; k++) {
//         string& good_string = (k == 0) ? good_string_1 : good_string_2;
//         int cost = 0;
//         for (int i = 0; i < N; i++) {
//             if (S[i] != good_string[i]) {
//                 cost += C[i];
//             }
//         }
//         min_cost = min(min_cost, cost);
//     }

//     // 最小コストの出力
//     cout << min_cost << endl;

//     return 0;
// }

