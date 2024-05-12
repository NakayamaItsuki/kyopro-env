
N, S = map(int, input().split())

As = [0] + list(map(int, input().split()))


dp = []

# 初期化
dp_i = [True] + [False] * S
dp.append(dp_i)

# メイン
for i in range(1, N+1):
    
    dp_i = []

    for j in range(S+1):

        # i-1番目までのカードでjが作れる場合
        if dp[i-1][j]:
            dp_i.append(True)
            continue
        
        # i-1番目までのカードでj-As[i]が作れる場合
        elif j - As[i] >= 0 and dp[i-1][j-As[i]]:
            dp_i.append(True)
            continue
        
        else :
            dp_i.append(False)

    dp.append(dp_i)

# if dp[N][S]:
#     print('Yes')
    
# else:
#     print('No')


# Noの場合の処理を済ましておく
if dp[N][S] == False:
    print('-1')
    exit()


# 最短経路の計算

i = N
j = S
route = []

while i > 0:
    
    #  i-1番目までのカードでjが作れる場合
    if dp[i-1][j]:
        i -= 1
        continue

    # i番目のカードを使う場合
    else:
        route.append(i)
        j -= As[i]
        i -= 1

route = route[::-1]

# 最短経路の長さを出力
print(len(route))

# 最短経路を出力
for r in route:
    print(r, end=' ')


