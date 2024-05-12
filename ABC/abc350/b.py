
N, Q = map(int, input().split())

Ts = list(map(int, input().split()))

from collections import Counter

counter = Counter(Ts)

cnt = 0

for value in counter.values():
    if value % 2 == 1:
        cnt += 1

print(N-cnt)


# print(counter)




