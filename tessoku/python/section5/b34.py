
N, X, Y = map(int, input().split())
As = list(map(int, input().split()))


# X = 2，Y = 3という条件なので，5ごとに繰り返す
grundy = [0, 0, 1, 1, 2]


flag = 0

for i in range(N):
    flag = flag ^ grundy[As[i] % 5]

if flag == 0:
    print("Second")
    
else:
    print("First")


