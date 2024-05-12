
S = input()

# シンプルな解法
# 2重ループを使っているので，O(N^2)かかる


# exchange_set = set()


# for i in range(len(S)):
#     for j in range(i + 1, len(S)):   
#         exchange_set.add(S[:i] + S[j] + S[i + 1:j] + S[i] + S[j + 1:])

# print(len(exchange_set))



# 高速な解法

# 各文字に注目する

s_set = set(S)

cnt = 0

from collections import Counter

s_counter = Counter(S)


for s, c in s_counter.items():
    cnt += c * (len(S) - c)

cnt = cnt // 2 # 重複を除去するために2で割る

# このままでは，同じ文字の入れ替え，例えばabccdにおいてcとcを入れ替えた時の文字列がカウントできていない．
# 2種類以上の文字列があったら，cntを1増やす必要がある

if max(s_counter.values()) >= 2:
    cnt += 1

print(cnt)






