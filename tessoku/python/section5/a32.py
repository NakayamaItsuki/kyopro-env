
N, A, B = map(int, input().split())

# dp[i] := 個数がiの時，打つ側の勝敗の状態
statuses = [False] * (N+1)


for i in range(N+1):
    
    if i >= A and statuses[i-A] == False: # 相手を負けさせる手がある場合は勝ち
        statuses[i] = True
        
    elif i >= B and statuses[i-B] == False: # 相手を負けさせる手がある場合は勝ち
        statuses[i] = True
    
    else: # 相手を負けさせる手がない場合は負け
        statuses[i] = False


if statuses[N] == True:
    print("First")
    
else:
    print("Second")
