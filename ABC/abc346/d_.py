
N = int(input())

S = input()

Cs = list(map(int, input().split()))


def min_cost_to_good_string(S, C):
    min_cost = float('inf')

    # 各位置での変更コストを計算
    for i in range(1, N):
        if S[i] == S[i-1]:
            # 現在の位置を変更しない場合のコスト
            cost_without_change = sum(C[j] for j in range(N) if j != i and j != i-1)
            # 現在の位置を変更する場合のコスト
            cost_with_change = cost_without_change + min(C[i], C[i-1])
            # 最小コストを更新
            min_cost = min(min_cost, cost_with_change)

    return min_cost if min_cost != float('inf') else 0

# サンプル入力データ
# S = "010101"
# C = [1, 2, 3, 4, 5, 6]

# # 最小コストの計算
# min_cost_to_good_string(S, C)

print(min_cost_to_good_string(S, Cs))


# def min_cost_to_good_string(S, C):
#     # N = len(S)
#     total_cost = 0
#     i = 0

#     while i < N-1:
#         if S[i] == S[i+1]:
#             # Find the end of this sequence of matching characters
#             j = i + 1
#             while j < N and S[j] == S[i]:
#                 j += 1
            
#             # Calculate the cost of changing this sequence, except one character
#             cost_of_sequence = sum(C[i:j]) - max(C[i:j])
#             total_cost += cost_of_sequence
#             i = j
#         else:
#             i += 1
    
#     return total_cost

# # Test the function with a sample input
# # S = "00100"
# # C = [1, 2, 3, 4, 5]
# # print(min_cost_to_good_string(S, Cs))

# total_cost = 0
































