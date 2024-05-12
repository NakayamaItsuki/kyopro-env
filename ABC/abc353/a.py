N = int(input())
Hs = list(map(int, input().split()))

ans = -1

for H in Hs[1:]:
    if H > Hs[0]:
        ans = Hs.index(H) + 1
        break

print(ans)







