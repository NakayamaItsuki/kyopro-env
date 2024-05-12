
N = int(input())

As = list(map(int, input().split()))

dp = [ [None]*(N+1) for _ in range(N+1) ]

# 初期値
for i in range(1, N+1):
    dp[N][i] = As[i-1]


for i in range(N-1, 0, -1):

    for j in range(1, i+1):

        if i%2 == 1:
            dp[i][j] = max(dp[i+1][j], dp[i+1][j+1])
        
        else:
            dp[i][j] = min(dp[i+1][j], dp[i+1][j+1])

print(dp[1][1])


