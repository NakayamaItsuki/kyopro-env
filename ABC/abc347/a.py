N, K = map(int, input().split())

As = list(map(int, input().split()))

for A in As:
    if A % K == 0:
        print(A//K, end=' ')






























