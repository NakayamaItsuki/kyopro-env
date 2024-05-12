
N = int(input())

As = [0,0] + list(map(int, input().split()))

Bs = [0,0,0] + list(map(int, input().split()))


dp = [-1] * (N+1)
P = [-1] * (N+1)


# スタート地点
dp[1] = 0
P[1] = 1

# 2つ目の地点
dp[2] = As[2]
P[2] = 1

# メイン
for i in range(3,N+1):
    
    from_i_1 = dp[i-1] + As[i]
    
    from_i_2 = dp[i-2] + Bs[i]
    
    # dp[i] = min(from_i_1, from_i_2)
    
    if from_i_1 < from_i_2:
        dp[i] = from_i_1
        P[i] = i-1
        
    else:
        dp[i] = from_i_2
        P[i] = i-2
    

# print(dp[N])

# 最短経路を復元する

i = N
ans = []

while True:
    ans.append(i)
    i = P[i]
    
    if i == 1:
        ans.append(1)
        break

# 逆順にする
ans = ans[::-1]


# 最短経路の長さを出力する
print(len(ans))

# 最短経路を出力する
for a in ans:
    print(a, end=" ")
    