
N = int(input())

As = [0, 0] + list(map(int, input().split()))

Bs = [0, 0, 0] + list(map(int, input().split()))

dp = [1000000000] * (N + 1) 
dp[1] = 0

for i in range(1, N):

    dp[i+1] = min(dp[i+1], dp[i] + As[i+1])

    if i <= N-2:
        dp[i+2] = min(dp[i+2], dp[i] + Bs[i+2])
    
print(dp[N])

