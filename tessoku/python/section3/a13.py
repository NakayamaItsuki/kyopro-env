N, K = map(int, input().split())

As = list(map(int, input().split()))

cnt = 0

R = 1

for i in range(N):
    
    diff = 0
    
    R -= 1 # 最初のR++用に減らしておく
    
    # diffがKを超えないギリギリまでRを増やす
    while diff <= K:
        R += 1
        
        # 最大データ数を超えたらbreak
        if R == N:
            break
        
        diff =  As[R] - As[i]

    R -= 1 # diffがKを超えたらRを戻す
    
    cnt += R - i
    

print(cnt)

