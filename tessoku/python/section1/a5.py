N , K = map(int, input().split())

cnt = 0

### ナイーブな解法 ###

# for i in range(1,N+1):
#     for j in range(i,N+1):
#         for k in range(j,N+1):
#             if i + j + k == K:
                
#                 if i == j and j == k:
#                     cnt += 1
                    
#                 elif i == j or j == k or k == i:
#                     cnt += 3
                    
#                 else:
#                     cnt += 6
            
#             # 高速化のため，すでに上限を超えたらループを抜ける
#             if i + j + k > K:
#                 break
        
#         if i + j > K:
#             break


### 高速化 ###

for i in range(1,N+1):
    for j in range(i,N+1):
        k = K - i - j # i,jが決まればkは一意に定まる
        
        # kが条件を満たすかどうかを判定
        if k >= j and k <= N: 
            if i == j and j == k:
                cnt += 1
            elif i == j or j == k or k == i:
                cnt += 3
            else:
                cnt += 6

print(cnt)