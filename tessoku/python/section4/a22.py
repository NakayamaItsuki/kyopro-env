
N = int(input())

As = list(map(int, input().split()))

Bs = list(map(int, input().split()))
    
dp = [-1000000000] * (N + 1) # 初期値は十分小さい値にしておく必要がある．初期値から行けないのにdp[i]が0だとおかしいから．
dp[1] = 0

for i in range(1, N):
    dp[As[i-1]] = max(dp[As[i-1]], dp[i] + 100)
    dp[Bs[i-1]] = max(dp[Bs[i-1]], dp[i] + 150)

print(dp[N])

