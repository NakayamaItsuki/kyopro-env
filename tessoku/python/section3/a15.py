N = int(input())

As = list(map(int, input().split()))

# 重複を取り除いて，ソートする
As_sorted = sorted(set(As))

# key:要素の値，value:その要素のインデックス，という辞書を作成
# 転置インデックスのようなもの
index_dict = {value: idx + 1 for idx, value in enumerate(As_sorted)}


for A in As:
    # print(As_sorted.index(A) + 1) # これだとO(N)かかる，ソート済みであることを活用できていない
    print(index_dict[A])
