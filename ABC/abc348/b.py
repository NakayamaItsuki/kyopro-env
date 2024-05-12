
N = int(input())

Xs, Ys = [], []

for i in range(N):
    X, Y = map(int, input().split())
    Xs.append(X)
    Ys.append(Y)

# print(Xs,Ys)

for i in range(N):
    
    max_dist = 0
    ans = None
    
    # 逆から距離を計算する
    for j in range(N-1, -1, -1):
        
        if i == j:
            continue
        
        dist = (Xs[i] - Xs[j])**2 + (Ys[i] - Ys[j])**2
        
        # print(i,j,dist)
        
        if max_dist <= dist:
            max_dist = dist
            ans = j+1

    print(ans)




















