N = int(input())

Xs = []
Ys = []

for i in range(N):
    X, Y = map(int, input().split())
    Xs.append(X)
    Ys.append(Y)

Q = int(input())

As, Bs, Cs, Ds = [0]*Q, [0]*Q, [0]*Q, [0]*Q

for i in range(Q):
    As[i], Bs[i], Cs[i], Ds[i] = map(int, input().split())

H = max(Xs)
W = max(Ys)

array_for_points = [ [0]*(W+1) for i in range(H+1) ]
SUM = [ [0]*(W+1) for i in range(H+1) ]

for i in range(N):
    array_for_points[Xs[i]][Ys[i]] += 1


# 累積和を計算

# 行方向で和を計算
for i in range(1,H+1):
    for j in range(1,W+1):
        SUM[i][j] = SUM[i][j-1] + array_for_points[i][j]

# 列方向で和を計算
for j in range(1,W+1):
    for i in range(1,H+1):
        SUM[i][j] += SUM[i-1][j]

for i in range(Q):
    print(SUM[Cs[i]][Ds[i]] - SUM[As[i]-1][Ds[i]] - SUM[Cs[i]][Bs[i]-1] + SUM[As[i]-1][Bs[i]-1])

