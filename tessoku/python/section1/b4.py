Ns = [int(i) for i in input()]

decimal = 0

# 1の位から順に2進数を10進数に変換
for i , N in enumerate(Ns[::-1]):
    decimal += N * (2 ** i)

print(decimal)
