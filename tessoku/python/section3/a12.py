N, K = map(int, input().split())

As = list(map(int, input().split()))


left = 0
right = 10**9 - 1

while left <= right:

    mid = (left + right) // 2

    # midの時の印刷枚数を計算
    X = 0
    for i in range(N):
        X += int(mid / As[i])
    
    # デバッグ
    # print('left:', left, 'right:', right, 'mid:', mid, 'X:', X)
    
    if X < K:
        left = mid + 1
    else:
        right = mid - 1
        
print(left)