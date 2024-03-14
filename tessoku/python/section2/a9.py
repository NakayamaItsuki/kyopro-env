H, W, N = map(int, input().split())

As, Bs, Cs, Ds = [0]*N, [0]*N, [0]*N, [0]*N

for i in range(N):
    As[i], Bs[i], Cs[i], Ds[i] = map(int, input().split())

### 注意：前後に余分にメモリを確保する必要がある．特に，この問題では後ろが余分に必要！！ ###
X = [ [0]*(W+1+1) for i in range(H+1+1) ]

for i in range(N):
    X[As[i]][Bs[i]] += 1
    X[Cs[i]+1][Ds[i]+1] += 1
    X[As[i]][Ds[i]+1] -= 1
    X[Cs[i]+1][Bs[i]] -= 1
    
    
# 累積和を計算
SUM = [ [0]*(W+1+1) for i in range(H+1+1) ]

# 行方向で和を計算
for i in range(1,H+1+1):
    for j in range(1,W+1+1):
        SUM[i][j] = SUM[i][j-1] + X[i][j]

# 列方向で和を計算
for j in range(1,W+1+1):
    for i in range(1,H+1+1):
        SUM[i][j] += SUM[i-1][j]

for i in range(1, H+1):
    for j in range(1, W+1):
        
        if j != 1:
            print(end = " ")
        
        print(SUM[i][j], end = "")
        
    print(end = "\n")
