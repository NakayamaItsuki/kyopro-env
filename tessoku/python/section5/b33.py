
N, H, W = map(int, input().split())
As, Bs = [], []

for i in range(N):
    A, B = map(int, input().split())
    As.append(A)
    Bs.append(B)


# 縦方向の山，横方向の山を考える．

flag = 0

for i in range(N):
    flag = flag ^ (As[i]-1)
    flag = flag ^ (Bs[i]-1)
    
if flag == 0:
    print("Second")
    
else:
    print("First")



