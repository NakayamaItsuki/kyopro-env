N = int(input())
As = list(map(int, input().split()))

K = 0
change_pair = []


for i in range(N):
    while As[i] != i + 1:
        j = As[i] - 1  # A[i]が本来あるべき位置
        
        # i番目とj番目をスワップ
        As[i], As[j] = As[j], As[i]
        
        K += 1
        # 1ベースで出力するために+1
        if i < j:
            change_pair.append([i + 1, j + 1])
        else:
            change_pair.append([j + 1, i + 1])

print(K)
for pair in change_pair:
    print(pair[0], pair[1])
