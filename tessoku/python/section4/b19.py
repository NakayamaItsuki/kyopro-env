
N, W = map(int, input().split())

ws, vs = [], []

for _ in range(N):
    w, v = map(int, input().split())
    ws.append(w)
    vs.append(v)


dp = []

# 初期値
dp_i = [0] + [1e11] * (100*1000)
dp.append(dp_i)


for i in range(1, N+1):
    dp_i = []
    
    # 価値：0から100*1000まで
    for v in range(100*1000+1):
        if v - vs[i-1] >= 0:
            dp_i.append(min(dp[i-1][v], dp[i-1][v-vs[i-1]] + ws[i-1]))
        else:
            dp_i.append(dp[i-1][v])
    
    dp.append(dp_i)
    
    
max_value = 0

for i in range(100*1000+1):
    
    # 重さがWを超える可能性がある．
    if dp[N][i] <= W:
        max_value = max(max_value, i)

print(max_value)

