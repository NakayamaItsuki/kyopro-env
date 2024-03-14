N = int(input())

As = [0] + list(map(int, input().split()))

D = int(input())

Ls = []
Rs = []

for i in range(D):
    L, R = map(int, input().split())
    Ls.append(L)
    Rs.append(R)

Ps = [0]*(N+1)
Qs = [0]*(N+1)


Ps[1] = As[1]
for i in range(2, N+1):
    Ps[i] = max(Ps[i-1], As[i])
    
Qs[N] = As[N]
for i in range(N-1, 0, -1):
    Qs[i] = max(Qs[i+1], As[i])

for i in range(D):
    print(max(Ps[Ls[i]-1], Qs[Rs[i]+1]))
