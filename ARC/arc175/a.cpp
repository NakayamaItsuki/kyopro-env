#include <iostream>
#include <vector>
#include <string>
using namespace std;

const int MOD = 998244353;

// DFS関数
int dfs(const vector<int>& P, string& S, int index, vector<bool>& taken) {
    if (index == S.size()) {
        // 全員がスプーンを取っているかチェック
        for (bool t : taken) {
            if (!t) return 0;
        }
        return 1;
    }

    int count = 0;
    int i = P[index] - 1;
    if (S[i] != '?') {
        // 利き手が決まっている場合
        int spoon = (S[i] == 'L') ? i : (i + 1) % S.size();
        if (!taken[spoon]) {
            taken[spoon] = true;
            count = dfs(P, S, index + 1, taken);
            taken[spoon] = false;
        }
    } else {
        // 利き手が不明な場合
        for (char hand : {'L', 'R'}) {
            int spoon = (hand == 'L') ? i : (i + 1) % S.size();
            if (!taken[spoon]) {
                taken[spoon] = true;
                S[i] = hand;
                count = (count + dfs(P, S, index + 1, taken)) % MOD;
                S[i] = '?';
                taken[spoon] = false;
            }
        }
    }
    return count;
}

int main() {
    int N;
    cin >> N;
    vector<int> P(N);
    for (int& p : P) cin >> p;
    string S;
    cin >> S;

    vector<bool> taken(N, false);
    cout << dfs(P, S, 0, taken) << endl;
    return 0;
}
