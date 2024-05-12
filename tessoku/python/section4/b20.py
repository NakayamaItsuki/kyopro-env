
S = input()
T = input()

dp = [ [ 0 ] * (len(T) + 1) for i in range(len(S) + 1) ]

# 初期化
for i in range(1,len(S)+1):
    dp[i][0] = i # i回の挿入操作
    
for j in range(1,len(T)+1):
    dp[0][j] = j # j回の削除操作
    
# dp
for i in range(1,len(S)+1):
    for j in range(1,len(T)+1):
        
        # 変更コスト
        if S[i-1]==T[j-1]:
            change_cost = 0
        else:
            change_cost = 1
            
        dp[i][j] = min(min(dp[i-1][j]+1, dp[i][j-1]+1), dp[i-1][j-1]+change_cost)
        
print(dp[len(S)][len(T)])
