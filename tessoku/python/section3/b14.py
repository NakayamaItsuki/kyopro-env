N, K = map(int, input().split())

As = list(map(int, input().split()))


# カードを半分に分割して、それぞれの組み合わせを全て求める

P = set()
Q = set()

half = N // 2

for i in range(2 ** half):
    p = 0
    for j in range(half):
        if (i >> j) & 1: # jビット目が立っているかどうか．iをjビット右にシフトして1（わかりやすく書くと，00...1）と論理積をとることで判定する
            p += As[j]
    P.add(p)

for i in range(2 ** (N - half)):
    q = 0
    for j in range(N - half):
        if (i >> j) & 1:
            q += As[j + half]
    Q.add(q)

# Qの中にK-P_iが存在するかどうかを調べる

for p in P:
    if K - p in Q:
        print("Yes")
        exit()
        
print("No")




