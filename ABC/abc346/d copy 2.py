
N = int(input())

S = input()

C = list(map(int, input().split()))


# N=5の時は
# 00がある場合
# 00101
# 10010
# 01001
# 10100

# 11がある場合
# 11010
# 01101
# 10110
# 01011

# N * 2のループが必要．
# 排他的論理和で変更する必要がある部分を見つける
# → 最小のコストを見つける

# # 良い文字列の全パターンを列挙する
    

def generate_good_strings(N):

    # 長さNのすべての良い文字列を生成する関数
    def generate_all_strings(N, s, result):
        if len(s) == N:
            result.append(s)
            return
        generate_all_strings(N, s + '0', result)
        generate_all_strings(N, s + '1', result)

    # 2つの連続する文字が同じかどうかをチェックする関数
    def is_good_string(s):
        count = 0
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                count += 1
        return count == 1

    all_strings = []
    good_strings = []

    generate_all_strings(N, '', all_strings)

    for s in all_strings:
        if is_good_string(s):
            good_strings.append(int(s, 2)) # 2進数を10進数に変換して追加
    
    return good_strings

good_strings = generate_good_strings(N)

min_cost = float('inf')

S = int(S, 2)

C = C[::-1]

for good_string in good_strings:

    # Sとの排他的論理和を取って，コストを計算する
    xor = S ^ good_string

    cost = 0
    for i in range(N):
        if xor & (1 << i):
            cost += C[i]

    min_cost = min(min_cost, cost)
    
print(min_cost)































