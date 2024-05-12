
N = int(input())
P = list(map(int, input().split()))
S = input()


mod = 998244353

# dp[i][j] = i人が確定しており，j人が未確定のときの場合の数

# dp = [[0] * (N + 1) for _ in range(N + 1)]



dp = [0] * (N + 1) # 人iまでの選択肢の合計
spoon = [1] * (N + 1) # スプーンiが残っているかどうか

# 初期化
dp[0] = 1 # 単位元


# 各人の操作について
for i in P:
    
    # 左利きでスプーンが残っている場合
    if i == 'L' & spoon[i] == 1:
        dp[i] = dp[i - 1]
        spoon[i] = 0
    
    # 右利きでスプーンが残っている場合
    elif i == 'R' & spoon[(i+1)//N] == 1:
        dp[i] = dp[i - 1]
        spoon[(i+1)//N] = 0

    # 利き手が定まっていない場合
    else:
        dp[i] = dp[i - 1] * 2
        spoon[i] = 1
        spoon[(i+1)//N] = 1





