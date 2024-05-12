#include <iostream>
#include <vector>
#include <set>
#include <cmath>

int main() {
    int N;
    std::cin >> N;

    std::vector<int> As(N);
    for (int i = 0; i < N; ++i) {
        std::cin >> As[i];
    }

    const int MOD = 998244353;
    long long ans = 0;

    // 桁数でグループ分け、各setを11個のvectorに保持
    std::vector<std::set<int>> grouped_As(11);

    for (int A : As) {
        int len = std::to_string(A).length();
        grouped_As[len].insert(A);
    }

    for (int A : As) {
        int lenA = std::to_string(A).length();
        grouped_As[lenA].erase(A); // 元の数をグループから削除

        for (int i = 0; i < 11; ++i) {
            long long sum_group = 0;
            for (int num : grouped_As[i]) {
                sum_group += num;
            }
            ans += grouped_As[i].size() * A * std::pow(10, i);
            ans += sum_group;
        }

        // grouped_As[lenA].insert(A); // 計算後、削除した数を再度追加
    }

    std::cout << ans % MOD << std::endl;

    return 0;
}
