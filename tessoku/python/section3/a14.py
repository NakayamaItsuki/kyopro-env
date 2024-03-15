N, K = map(int, input().split())

As = list(map(int, input().split()))
Bs = list(map(int, input().split()))
Cs = list(map(int, input().split()))
Ds = list(map(int, input().split()))

### ステップ1 ###
# まず、AとBの組み合わせを全て求める

P = set()

for a in As:
    for b in Bs:
        P.add(a + b)
        

# 同様に，CとDの組み合わせを全て求める

Q = set()

for c in Cs:
    for d in Ds:
        Q.add(c + d)

### ステップ2 ###
# Qの中にK-P_iが存在するかどうかを調べる

flag = False

for p in P:
    if K - p in Q:
        flag = True
        break

if flag:
    print("Yes")

else:
    print("No")


