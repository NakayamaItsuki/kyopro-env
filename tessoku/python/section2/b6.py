N = int(input())

As = [int(i) for i in input().split()]

Q = int(input())

Ls = []
Rs = []

for i in range(Q):
    L, R = map(int, input().split())
    Ls.append(L)
    Rs.append(R)

# 累積和
cumulative_sums = [0] # 0日目の累積和は0

for i in As:
    cumulative_sums.append(cumulative_sums[-1] + i)

for i in range(Q):
    num_atari = cumulative_sums[Rs[i]] - cumulative_sums[Ls[i]-1]
    num_hazure = (Rs[i] - Ls[i] + 1) - num_atari

    if num_atari > num_hazure:
        print("win")
    elif num_atari < num_hazure:
        print("lose")
    else:
        print("draw")    
