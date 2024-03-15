N = int(input())

As = list(map(int, input().split()))

Q = int(input())

Xs = list(int(input()) for _ in range(Q))

import bisect

As.sort()

for X in Xs:
    # As_i <= X を満たす最大のiの，スタートからの位置を返す
    print(bisect.bisect_left(As, X))
