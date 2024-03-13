N = int(input())

binary = []

for i in range(10):
    binary.append(N % 2)
    N = N // 2

for i in binary[::-1]:
    print(i, end="")