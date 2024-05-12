
N = int(input())
S = input()

dp = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

# 初期値の設定
for i in range(1, N+1):
    dp[i][i] = 1
    if i <= N - 1:
        if S[i - 1] == S[i]:
            dp[i][i + 1] = 2
        else:
            dp[i][i + 1] = 1


# DPテーブルの更新
for length in range(2, N):
    for l in range(1, N - length + 1):
        
        r = l + length
        
        if S[l - 1] == S[r - 1]:
            dp[l][r] = max(dp[l][r - 1], dp[l + 1][r], dp[l + 1][r - 1] + 2)
        
        else:
            dp[l][r] = max(dp[l + 1][r], dp[l][r - 1])


print(dp[1][N])
