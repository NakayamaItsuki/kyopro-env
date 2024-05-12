
N = int(input())

As = []
Bs = []

for i in range(N):
    As.append(list(input()))
    
for i in range(N):
    Bs.append(list(input()))

# print(As, Bs)
    
for i in range(N):
    for j in range(N):
        if As[i][j] != Bs[i][j]:
            print(i+1, j+1)
