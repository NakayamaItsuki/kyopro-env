
N, W = map(int, input().split())

ws, vs = [], []

for _ in range(N):
    w, v = map(int, input().split())
    ws.append(w)
    vs.append(v)


dp = []

# 初期値
dp_i = [0] + [-1e11] * (W)
dp.append(dp_i)


for i in range(1, N+1):
    dp_i = []
    
    # 重さ:0からWまで
    for w in range(W+1):
        if w - ws[i-1] >= 0:
            dp_i.append(max(dp[i-1][w], dp[i-1][w-ws[i-1]] + vs[i-1]))
        else:
            dp_i.append(dp[i-1][w])
    
    dp.append(dp_i)


# 重さがWピッタリの時に，価値が最大とは限らないので，最大値を見つける必要がある．

max_value = 0

for i in range(W+1):
    max_value = max(max_value, dp[N][i])

print(max_value)