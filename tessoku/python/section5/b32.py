
N, K = map(int, input().split())
As = list(map(int, input().split()))

# dp[i] := 山の石がi個の時，打つ側の勝敗の状態
statuses = [False] * (N+1)


for i in range(N+1):
    
    # 全ての取り出し方について
    for A in As:
        if i >= A and statuses[i-A] == False: # 相手を負けさせる手があるなら勝ち
            statuses[i] = True

if statuses[N] == True:
    print("First")

else:
    print("Second")

