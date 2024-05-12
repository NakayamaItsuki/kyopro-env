
N = int(input())

As = [0,0] + list(map(int, input().split()))

Bs = [0,0,0] + list(map(int, input().split()))


dp = [-1] * (N+1)

# スタート地点
dp[1] = 0

# 2つ目の地点
dp[2] = As[2]

# メイン
for i in range(3,N+1):
    
    from_i_1 = dp[i-1] + As[i]
    
    from_i_2 = dp[i-2] + Bs[i]
    
    dp[i] = min(from_i_1, from_i_2)

print(dp[N])

