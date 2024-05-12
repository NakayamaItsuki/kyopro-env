N, A, B = map(int, input().split())

S = input()

# iとjの入れ替え：A
# iの置き換え：B
# 最小コストを求める

def min_cost_to_valid_parentheses(S, A, B):
    N = len(S)
    dp = [[float('inf')] * N for _ in range(N)]

    # 初期化: 空の部分文字列のコストは0
    for i in range(N):
        dp[i][i] = 0

    # dpテーブルの更新
    for length in range(2, N + 1):
        for i in range(N - length + 1):
            j = i + length - 1
            # 直接文字を変更する場合
            if length == 2:
                dp[i][j] = 0 if (S[i] == '(' and S[j] == ')') else B
            else:
                # 文字を変更する場合
                dp[i][j] = min(dp[i][j], B + dp[i+1][j])
                # iとkをスワップ（または変更）し、2つの部分問題に分ける
                for k in range(i+1, j):
                    dp[i][j] = min(dp[i][j], (A if S[i] != S[k] else 0) + dp[i+1][k-1] + dp[k+1][j])

    return dp[0][N-1]

# 例：S = "(()())", A = 3, B = 2
# S = "(()())"
# A = 3
# B = 2
min_cost = min_cost_to_valid_parentheses(S, A, B)
min_cost

print(min_cost)
