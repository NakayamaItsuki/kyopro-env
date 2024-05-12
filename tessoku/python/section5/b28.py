
N = int(input())

# フィボナッチ数列

MOD = 10**9 + 7

a, b = 1, 1

for i in range(3, N+1):

    c = (a + b) % MOD # だんだん値が大きくなるので，MODを取る
    
    a = b
    b = c

print(c)

