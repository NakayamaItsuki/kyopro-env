N, Q = map(int, input().split())

As = [int(i) for i in input().split()]

LRs = []

for i in range(Q):
    LRs.append([int(i) for i in input().split()])
    
# 累積和
cumulative_sums = [0] # 0日目の累積和は0

sum = 0
for i in As:
    sum += i
    cumulative_sums.append(sum)

for LR in LRs:
    print(cumulative_sums[LR[1]] - cumulative_sums[LR[0]-1])
