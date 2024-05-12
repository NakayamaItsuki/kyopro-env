
H, W = map(int, input().split())

# 全体でH+W-2回移動する必要があり，そのうちH-1回は下に移動する必要がある．つまり，(H+W-2)C(H-1)を求めれば良い．
a = (H-1)+(W-1)
b = H-1

MOD = 10**9 + 7

# 素数MODで割った余りを求める際，/ b を * b ^(M-2)に変換できる，という性質を利用する

# nCr = n! / (r! * (n-r)! ) = n! * (r! * (n-r)!)^(M-2)


# n!
n_pow = 1

for i in range(1, a+1):
    n_pow *= i
    n_pow %= MOD


# r! * (n-r)!
r_pow = 1
n_r_pow = 1

for i in range(1, b+1):
    r_pow *= i
    r_pow %= MOD

for i in range(1, a-b+1):
    n_r_pow *= i
    n_r_pow %= MOD

r_pow_mul_n_r_pow = r_pow * n_r_pow % MOD

# print(n_pow, r_pow, n_r_pow, r_pow_mul_n_r_pow)

# (r! * (n-r)!)^(M-2)

# 繰り返し二乗法

def Power(a, b, MOD):
    p = a
    ans = 1
    for i in range(30): # log2(10^9) = 29.9，つまり，10^9<2^30よって，30回で十分
        if (b // 2**i) % 2 ==1: # bを2進数に変換して，i桁目が1かどうか
            ans *= p
            ans %= MOD
        p = p**2 % MOD
    return ans

print(n_pow * Power(r_pow_mul_n_r_pow, MOD-2, MOD) % MOD)

