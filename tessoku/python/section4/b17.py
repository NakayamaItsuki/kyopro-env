
N = int(input())

hs = [0] + list(map(int, input().split()))

dp = [-1] * (N+1)
P = [-1] * (N+1)

# スタート地点
dp[1] = 0
P[1] = 1

# 2つ目の地点
dp[2] = abs(hs[1]-hs[2])
P[2] = 1


for i in range(3,N+1):
    
    from_i_1 = dp[i-1] + abs(hs[i-1]-hs[i])
    
    from_i_2 = dp[i-2] + abs(hs[i-2]-hs[i])
    
    # dp[i] = min(from_i_1, from_i_2)
    
    if from_i_1 < from_i_2:
        dp[i] = from_i_1
        P[i] = i-1
        
    else:
        dp[i] = from_i_2
        P[i] = i-2
    

# print(dp[N])

i = N
route = []

while True:
    route.append(i)
    i = P[i]

    if i == 1:
        route.append(1)
        break

# 逆順にする
route = route[::-1]


# 最短経路の長さを出力する
print(len(route))

# 最短経路を出力する
for r in route:
    print(r,end=" ")

