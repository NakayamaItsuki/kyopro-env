
N = int(input())

S = input()

C = list(map(int, input().split()))


# def generate_good_strings(N):

#     # 長さNのすべての良い文字列を生成する関数
#     def generate_all_strings(N, s, result):
#         if len(s) == N:
#             result.append(s)
#             return
#         generate_all_strings(N, s + '0', result)
#         generate_all_strings(N, s + '1', result)

#     # 2つの連続する文字が同じかどうかをチェックする関数
#     def is_good_string(s):
#         count = 0
#         for i in range(len(s) - 1):
#             if s[i] == s[i + 1]:
#                 count += 1
#         return count == 1

#     all_strings = []
#     good_strings = []

#     generate_all_strings(N, '', all_strings)

#     for s in all_strings:
#         if is_good_string(s):
#             good_strings.append(int(s, 2)) # 2進数を10進数に変換して追加
    
#     return good_strings

### 効率良く良い文字列を生成する ###
# good_strings = []

# # N-1文字の101010..or 010101..を生成する
# string_start_0 = '0' + '10' * (N//2)
# string_start_1 = '1' + '01' * (N//2)

# # どこに0または1を入れるかを考える
# for i in range(N):
#     good_strings.append(int(string_start_0[:N], 2))

def generate_good_strings(N):
    good_strings = []

    # パターン1: 先頭に連続する2つの同じ文字、残りは異なる文字
    for i in range(2, N + 1):
        good_strings.append('1' * i + '0' * (N - i))  # 先頭が1
        good_strings.append('0' * i + '1' * (N - i))  # 先頭が0

    # パターン2: 最初の文字と異なる2文字が連続し、残りは最初の文字と同じ
    if N > 2:
        for i in range(1, N - 1):
            good_strings.append('1' * i + '01' + '1' * (N - i - 2))  # 先頭が1
            good_strings.append('0' * i + '10' + '0' * (N - i - 2))  # 先頭が0

    # 二進数を十進数に変換
    return [int(s, 2) for s in good_strings]

good_strings = generate_good_strings(N)

print(good_strings)

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






