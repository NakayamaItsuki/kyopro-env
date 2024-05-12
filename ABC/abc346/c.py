
N, K = map(int, input().split())
As = list(map(int, input().split()))

As_set = set(As)

### forループは厳しそう ###
# sum = 0

# for i in range(1, K+1):
    
#     if i not in As_set:
#         sum += i

# print(sum)

# sum_As_set = sum(As_set)

sum_As_set_lower_than_K = [i for i in As_set if i <= K]

sum_1_to_K = K*(K+1)//2

# print(sum_1_to_K)
# print(sum_As_set)
# print(sum_As_set_lower_than_K)

# print(sum_1_to_K - sum_As_set)
print(sum_1_to_K - sum(sum_As_set_lower_than_K))


### メモ ###
# pythonのsetはO(1)だが，特定の悪意のある入力に対して遅くなることがある（ハッシュを使ってるからっぽい）
# Hackされないコード↓
"""
import random
R = random.randint(1, 1 << 60)
N, K = map(int, input().split())
A = list(map(int, input().split()))
S = set([i ^ R for i in A]) # hack を防ぐため，i の代わりに i ^ R を用いる
ans = K*(K+1)//2
for j in S:
    i = j ^ R  # 元に戻す
    if i <= K:
        ans -= i
print(ans)
"""
























