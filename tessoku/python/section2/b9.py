N = int(input())

As, Bs, Cs, Ds = [0]*N, [0]*N, [0]*N, [0]*N

for i in range(N):
    As[i], Bs[i], Cs[i], Ds[i] = map(int, input().split())
    
    # 問題用に調整する
    Cs[i] -= 1
    Ds[i] -= 1

H = 1500
W = 1500

X = [ [0]*(W+1+1) for i in range(H+1+1) ]

for i in range(N):
    X[As[i]][Bs[i]] += 1
    X[Cs[i]+1][Ds[i]+1] += 1
    X[As[i]][Ds[i]+1] -= 1
    X[Cs[i]+1][Bs[i]] -= 1


SUM = [ [0]*(W+1+1) for i in range(H+1+1) ]

# SUMの端っこを埋める
for i in range(0, H+1+1):
    SUM[i][0] = X[i][0]
    
for j in range(0, W+1+1):
    SUM[0][j] = X[0][j]
    

# 行方向で和を計算
for i in range(0,H+1+1):
    for j in range(1,W+1+1):
        SUM[i][j] = SUM[i][j-1] + X[i][j]

# 列方向で和を計算
for j in range(0,W+1+1):
    for i in range(1,H+1+1):
        SUM[i][j] += SUM[i-1][j]

cnt = 0

for i in range(0, H+1):
    for j in range(0, W+1):
        if SUM[i][j] > 0:
            cnt += 1

print(cnt)


