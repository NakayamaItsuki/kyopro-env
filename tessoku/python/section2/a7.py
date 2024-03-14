D = int(input())
N = int(input())

Ls, Rs = [], []

for i in range(N):
    L, R = map(int, input().split())
    Ls.append(L)
    Rs.append(R)

# 前日比を格納する配列
compared_to_the_previous_day = [0] * (D+1+1) # 0日目とD+1日目も含む

for i in range(N):
    compared_to_the_previous_day[Ls[i]] += 1 # 参加者が増える
    compared_to_the_previous_day[Rs[i]+1] -= 1 # 参加者が減る

num_attendees = 0
for i in range(1, D+1):
    num_attendees += compared_to_the_previous_day[i]
    print(num_attendees)
