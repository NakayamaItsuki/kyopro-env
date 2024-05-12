
N, X, Y = map(int, input().split())
As = list(map(int, input().split()))


grundy = [False] * (max(As)+1)

# 最大の山について，Grundy数を求める
for i in range(max(As)+1):
    
    can_transit = [False] * 3
    
    if i >= X: 
        can_transit[grundy[i-X]] = True # grundy[i-X]の状態に遷移できる
        
    if i >= Y:
        can_transit[grundy[i-Y]] = True # grundy[i-Y]の状態に遷移できる
    
    
    if can_transit[0] == False: # 0に遷移できないならGrundy数は0
        grundy[i] = 0
    
    elif can_transit[1] == False: # 0には遷移できるが，1に遷移できないならGrundy数は1
        grundy[i] = 1
        
    else: # 0にも1にも遷移できるならGrundy数は2
        grundy[i] = 2


flag = 0

for i in range(N):
    flag = flag ^ grundy[As[i]]

if flag == 0:
    print("Second")
    
else:
    print("First")


