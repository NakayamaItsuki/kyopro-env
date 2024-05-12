
N = int(input())

Ps, As = [0], [0] # indexが1から始まるようにするために0を追加

for _ in range(N):
    P, A = map(int, input().split())
    Ps.append(P)
    As.append(A)
    
Ps.append(0) # indexがN+1になるように0を追加
As.append(0) # indexがN+1になるように0を追加


dp = [ [ 0 ] * (N + 2) for i in range(N + 2) ] # indexが0とN+1の分を追加

for l in range(1,N):
    for r in range(N, l-1, -1): # N-1からlまで-1ずつ減らす
        
        # 左端を取り除いた場合のスコア
        if l<= Ps[l-1] <= r:
            erase_left = dp[l-1][r] + As[l-1]
        
        else :
            erase_left = dp[l-1][r]
            
        
        # 右端を取り除いた場合のスコア
        if l<= Ps[r+1] <= r:
            erase_right = dp[l][r+1] + As[r+1]
        
        else :
            erase_right = dp[l][r+1]

        dp[l][r] = max(erase_left, erase_right)


max_score = 0

for i in range(1,N):
    max_score = max(max_score, dp[i][i])
    
print(max_score)


