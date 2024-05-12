N = int(input())

As = list(map(int, input().split()))

# As = [A % 1e8 for A in As]

# print(2 * sum(As))


# ans = 0

# for i in range(N):
#     for j in range(i + 1, N):
#         ans += (As[i] + As[j]) % 1e8

# print(int(ans))


sum_A = sum(As)


# print((N-1) * int(sum_A))

# 二分探索を活用し，足した時に10^8を超えるペアの総数を求める
# 二分探索を活用するために，ソートする
As.sort()

# 二分探索を活用するために，累積和を求める
# cumsum = [0]
# for i in range(N):
#     cumsum.append(cumsum[-1] + As[i])
    

# # 二分探索を活用するために，足した時に10^8を超えるペアの総数を求める
# cnt_pairs = 0
# for i in range(N):
#     # 二分探索で，As[i] + As[j] >= 10^8を満たす最小のjを求める
#     left = i
#     right = N
#     while right - left > 1:
#         mid = (left + right) // 2
#         if As[i] + As[mid] >= 1e8:
#             right = mid
#         else:
#             left = mid
#     # ans += (N - right) * As[i] + cumsum[right]
#     cnt_pairs += N - right


# from bisect import bisect_left

# cnt_pairs = 0

# print(As)

# # 各要素に対して、和がtarget_sumを超えるペアを数える
# for i in range(len(As)):
#     # 和がtarget_sumを超える最小のセカンド要素のインデックスを見つける
#     j = bisect_left(As, 1e8 - As[i] + 1)
    
    
#     if j == len(As):
#         continue
    
#     if As[i] > 5e7:
#         cnt_pairs += len(As) - j - 1

#     else:
#         cnt_pairs += len(As) - j
        
#     print(j, cnt_pairs)

# cnt_pairs //= 2

# print(cnt_pairs)
    
# print(int((N-1) * sum_A - cnt_pairs * 1e8))


from bisect import bisect_left

count = 0

# Iterate through each number
for i in range(N):
    # Find the minimum index j where numbers[i] + numbers[j] > target_sum
    # Note: Start the search from i+1 to avoid counting pairs with themselves
    j = bisect_left(As, 1e8 - As[i], i + 1, N)
    # Add the number of valid pairs from j to the end of the list
    count += N - j

# print(count)

print(int((N-1) * sum_A - count * 1e8))
