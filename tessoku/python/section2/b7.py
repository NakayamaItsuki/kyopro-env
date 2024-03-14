T = int(input())
N = int(input())

Ls, Rs = [], []

for i in range(N):
    L, R = map(int, input().split())
    Ls.append(L)
    Rs.append(R)

# 前時比を格納する配列
compared_to_the_previous_time = [0] * (T+1+1) # 0時とT+1時も含む

for i in range(N):
    compared_to_the_previous_time[Ls[i]] += 1 # 従業員が増える
    compared_to_the_previous_time[Rs[i]] -= 1 # 従業員が減る

num_workers = 0
for i in range(0, T):
    num_workers += compared_to_the_previous_time[i]
    print(num_workers)
