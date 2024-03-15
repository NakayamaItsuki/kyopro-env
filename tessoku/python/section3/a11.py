N, X = map(int, input().split())

As = list(map(int, input().split()))

left = 0
right = N-1

# 二分探索，最終的にleftが探索要素のインデックスになる
while left <= right:
    mid = (left + right) // 2
    if As[mid] < X:
        left = mid + 1
    else:
        right = mid - 1

print(left+1)

