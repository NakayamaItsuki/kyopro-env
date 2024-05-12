N = int(input())

As = list(map(int, input().split()))

MOD = 998244353

ans = 0

# 桁数でグループ分け
# grouped_As = [[] for _ in range(11)]
grouped_As = [ set() for i in range(11)]

for A in As:
    # print(len(str(A)))
    # grouped_As[len(str(A))].append(A)
    grouped_As[len(str(A))].add(A)

print(grouped_As)

# sum_grouped_As = [sum(grouped_As[i]) for i in range(11)]

for A in As:
    
    # 削除
    # grouped_As[len(str(A))].remove(A)
    grouped_As[len(str(A))].discard(A)
    
    for i in range(11):
        ans += len(grouped_As[i]) * A * 10 ** i # 10 ** iは桁数を表す
        ans += sum(grouped_As[i])
        # ans += sum_grouped_As[i]
    
    # print(ans)
    
print(ans % MOD)