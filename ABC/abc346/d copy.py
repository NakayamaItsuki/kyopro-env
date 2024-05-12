
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
# for i in range(N):
    

def generate_good_strings(N):
    # Function to generate all binary strings of length N
    def generate_all_strings(N, s, result):
        if len(s) == N:
            result.append(s)
            return
        generate_all_strings(N, s + '0', result)
        generate_all_strings(N, s + '1', result)

    # Function to check if a binary string is a good string
    def is_good_string(s):
        count = 0
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                count += 1
        return count == 1

    all_strings = []
    good_strings = []

    # Generate all binary strings of length N
    generate_all_strings(N, '', all_strings)

    # Filter out the good strings
    for s in all_strings:
        if is_good_string(s):
            # good_strings.append(s)
            good_strings.append(int(s, 2)) # 2進数を10進数に変換して追加
            
            # デバッグ
            # print(s)

    return good_strings

good_strings = generate_good_strings(N)
# print(good_strings)

min_cost = float('inf')

S = int(S, 2)

print('S',S)

print('C',C)

C = C[::-1]

for good_string in good_strings:

    # Sとの排他的論理和を取って，コストを計算する
    xor = S ^ good_string
    # cost = sum(C[i+1] for i in range(N-1) if xor & (1 << i))
    
    cost = 0
    for i in range(N):
        if xor & (1 << i):
            cost += C[i]
    
    # 2進数で表示
    # print(bin(good_string), bin(S))
    
    # print(int(bin(good_string), 2), int(bin(S), 2))
    print(good_string, cost)
    
    # print(cost)
    
    min_cost = min(min_cost, cost)
    
print(min_cost)































