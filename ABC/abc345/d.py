
N, H, W = map(int, input().split())

As = []
Bs = []

for _ in range(N):
    A, B = map(int, input().split())
    As.append(A)
    Bs.append(B)


# ビット全探索，3進数のバージョン
# 0：使わない
# 1：そのまま使う
# 2：90度回転して使う

# 全パターン列挙
subsets_set = set()

for i in range(3**N):
    subset = []
    
    for j in range(N):
        # subset.append(i // (3 ** j) % 3)
        
        # そのまま使う
        if i // (3 ** j) % 3 == 1:
            subset.append((As[j], Bs[j]))
        
        # 90度回転して使う        
        elif i // (3 ** j) % 3 == 2:
            subset.append((Bs[j], As[j]))
        
    # print(subset)
    
    subsets_set.add(tuple(subset))
    
print(subsets_set)


flag = False

# 各サブセットについて，埋められるかどうか調べる


def can_fill(subset_list, H, W):

    # マス目を初期化
    grid = [[0 for _ in range(W)] for _ in range(H)]
    
    
    for a, b in subset_list:

        # 縦と横の総当たりでブロックが置けるかどうか調べる
        for i in range(H):
            for j in range(W):
                
                if i + a <= H and j + b <= W:
                    flag = True
                    for k in range(a):
                        for l in range(b):
                            if grid[i + k][j + l] == 1:
                                flag = False
                                break
                        if not flag:
                            break
                    if flag:
                        for k in range(a):
                            for l in range(b):
                                grid[i + k][j + l] = 1
                        break
    
    
    


for subset in subsets_set:
    
    subset_list = list(subset)
    
    if can_fill(subset_list, H, W):
        flag = True
        break
    
if flag:
    print("Yes")

else:
    print("No")







