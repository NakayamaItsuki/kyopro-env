
N = int(input())

As = [ None ] * (N+1)
# for i in range(1, N+1):
for i in range(N):
	As[i] = list(map(int, input().split()))

# dp[通った都市][今いる都市] := 距離の総和の最小値
dp = [ [ 10 ** 9 ] * N for i in range(2 ** N) ]

# 動的計画法
dp[0][0] = 0

for i in range(2**N):
    for j in range(N):
        
        if dp[i][j] == 10**9:
            continue
        
        else :
            for k in range(N): # 今いる都市jから都市kに移動する
                if (i // (2 ** k) % 2) == 0: # 2のk乗で割り切れるなら，k番目の都市はまだ通っていない
                    # dp[i + 2**k][k] = min(dp[i + 2**k][k], dp[i][j] + ( (As[j][0]-As[k][0])**2 + (As[j][1]-As[k][1])**2 ) ** 0.5)
                    
                    distance = ( (As[j][0]-As[k][0])**2 + (As[j][1]-As[k][1])**2 ) ** 0.5
                    dp[i + 2**k][k] = min(dp[i + 2**k][k], dp[i][j] + distance)
        
        
print(dp[2**N-1][0])