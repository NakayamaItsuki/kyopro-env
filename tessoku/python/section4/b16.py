
N = int(input())

hs = [0] + list(map(int, input().split()))

dp = [-1] * (N+1)

# スタート地点
dp[1] = 0

# 2つ目の地点
dp[2] = abs(hs[1]-hs[2])


for i in range(3,N+1):
    
    from_i_1 = dp[i-1] + abs(hs[i-1]-hs[i])
    
    from_i_2 = dp[i-2] + abs(hs[i-2]-hs[i])
    
    dp[i] = min(from_i_1, from_i_2)
    

print(dp[N])




