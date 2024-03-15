N, K = map(int, input().split())

As = [0] + list(map(int, input().split()))

cnt = 0

# 累積和を計算
cumsum = [0] * (N+1+1) # 0番目の要素を追加しておく

for i in range(1, N+1):
    cumsum[i] = cumsum[i-1] + As[i]

R = 1


for i in range(1,N+1):
    
    sum = cumsum[R] - cumsum[i-1]
    
    while R <= N and sum <= K:
        R += 1
        sum = cumsum[R] - cumsum[i-1]
    
    R -= 1 # sumがKを超えたらRを戻す，メモ：模範解答はRを戻す代わりに，cumsum[R+1] - cumsum[i-1]としている
    
    cnt += R - i + 1
    
print(cnt)