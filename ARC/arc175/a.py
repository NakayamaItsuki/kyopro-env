
N = int(input())
P = [0] + list(map(int, input().split()))
S = input()

S = ' ' + S

import math

mod = 998244353

# 木構造を使用する

# もし，左利きなら左の子の値を自身の値にする
# もし，右利きなら右の子の値を自身の値にする
# どちらでもないなら，左右の子の値の和を自身の値にする
# 末端のノードは1を返す

cnt = 0

spoon = [None] + [1] * (N + 1) # スプーンiが残っているかどうか


def dfs(v):
    

    # もし，末端のノードなら，spoonが取れるかどうかを返す
    if v >= 2**N:
        
        idx = int(math.log2(v)) + 1
        
        if S[idx] == 'L':
            if spoon[idx] == 1:
                spoon[idx] = 0
                return 1
            else:
                return 0
            
        elif S[idx] == 'R':
            if spoon[(idx+1)%N] == 1:
                spoon[(idx+1)%N] = 0
                return 1
            else:
                return 0
        
        else:
            if spoon[idx] == 1:
                spoon[idx] = 0
                left = 1
                spoon[idx] = 1
                if spoon[(idx+1)%N] == 1:
                    spoon[(idx+1)%N] = 0
                    right = 1
                    spoon[(idx+1)%N] = 1
                    return left + right
                else:
                    return left
            else:
                left = 0
                if spoon[(idx+1)%N] == 1:
                    spoon[(idx+1)%N] = 0
                    right = 1
                    spoon[(idx+1)%N] = 1
                    return left + right
                else:
                    return left
                
    # そうでないなら，左右の子の値を計算して，自身の値を返す
    else :
        
        idx = int(math.log2(v)) + 1
        
        # 左利きの場合
        if S[idx] == 'L':
            spoon[idx] = 0
            tmp = dfs(v * 2)
            spoon[idx] = 1
            return tmp
        
        # 右利きの場合
        elif S[idx] == 'R':
            spoon[(idx+1)%N] = 0
            tmp = dfs(v * 2 + 1)
            spoon[(idx+1)%N] = 1
            return tmp
    
        # どちらでもない場合
        else:
            idx = int(math.log2(v)) + 1
            spoon[idx] = 0
            left = dfs(v * 2)
            spoon[idx] = 1
            
            spoon[(idx+1)%N] = 0
            right = dfs(v * 2 + 1)
            spoon[(idx+1)%N] = 1
            
            return (left + right) % mod
        
print(dfs(1))
    
    
    
    
    