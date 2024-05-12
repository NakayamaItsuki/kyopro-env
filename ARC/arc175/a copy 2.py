
N = int(input())
P = list(map(int, input().split()))
S = input()

S = ' ' + S

import math

mod = 998244353

# 木構造を使用する

# もし，左利きなら左の子の値を自身の値にする
# もし，右利きなら右の子の値を自身の値にする
# どちらでもないなら，左右の子の値の和を自身の値にする
# 末端のノードは1を返す

tree = [0] * 2**(N+1)

spoon = [1] * (N + 1) # スプーンiが残っているかどうか

def dfs(v):
    if v >= 2**N:
        if S[v] == 'L':
            if spoon[v] == 1:
                spoon[v] = 0
                return 1
            else:
                return 0
        elif S[v] == 'R':
            if spoon[(v+1)%N] == 1:
                spoon[(v+1)%N] = 0
                return 1
            else:
                return 0
        else:
            if spoon[v] == 1:
                spoon[v] = 0
                left = 1
                spoon[v] = 1
                if spoon[(v+1)%N] == 1:
                    spoon[(v+1)%N] = 0
                    right = 1
                    spoon[(v+1)%N] = 1
                    return left + right
                else:
                    return left
            else:
                left = 0
                if spoon[(v+1)%N] == 1:
                    spoon[(v+1)%N] = 0
                    right = 1
                    spoon[(v+1)%N] = 1
                    return left + right
                else:
                    return left

        
    v = int(math.log2(v)) + 1 
    
    if S[v] == 'L':
        spoon[v] = 0
        tree[v] = dfs(v * 2)
    elif S[v] == 'R':
        spoon[(v+1)%N] = 0
        tree[v] = dfs(v * 2 + 1)
    else:
        spoon[v] = 0
        left = dfs(v * 2)
        spoon[v] = 1
        
        spoon[(v+1)%N] = 0
        right = dfs(v * 2 + 1)
        spoon[(v+1)%N] = 1
        
        tree[v] = left + right        
        
    return tree[v]

print(dfs(1) % mod)




