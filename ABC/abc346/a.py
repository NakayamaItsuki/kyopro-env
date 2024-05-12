N = int(input())

As = list(map(int, input().split()))
Bs = []

for i in range(N-1):
    Bs.append(As[i]*As[i+1])

for i in range(N-1):
    print(Bs[i], end=" ")
































