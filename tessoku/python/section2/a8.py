H, W = map(int, input().split())

# X = [ [0]*(W+1) ] * (H+1)

X = [ [0]*(W+1) ]

for i in range(1,H+1):
    
    X.append([0] + list(map(int, input().split())))
        
Q = int(input())

As, Bs, Cs, Ds = [0]*Q, [0]*Q, [0]*Q, [0]*Q
for i in range(Q):
    As[i], Bs[i], Cs[i], Ds[i] = map(int, input().split())
    
# 累積和を計算

# SUM = [ [0]*(W+1) ] * (H+1) # これ，ダメ．参照がコピーされるから．

SUM = [ [ 0 ] * (W + 1) for i in range(H + 1) ]

# 行方向で和を計算
for i in range(1,H+1):
    for j in range(1,W+1):
        SUM[i][j] = SUM[i][j-1] + X[i][j]

# 列方向で和を計算
for j in range(1,W+1):
    for i in range(1,H+1):
        SUM[i][j] += SUM[i-1][j]

for i in range(Q):
    print(SUM[Cs[i]][Ds[i]] - SUM[As[i]-1][Ds[i]] - SUM[Cs[i]][Bs[i]-1] + SUM[As[i]-1][Bs[i]-1])

