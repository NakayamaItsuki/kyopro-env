
a, b = map(int, input().split())

MOD = 10**9 + 7


# 繰り返し二乗法

p = a

ans = 1

# a^42をa^2+a^8+a^32に分解する
# 42 = 2^5 + 2^3 + 2^1

for i in range(30): # log2(10^9) = 29.9，つまり，10^9<2^30．よって，30回で十分
    
    if int(b / 2**i) % 2 ==1: # bを2進数に変換して，i桁目が1かどうか
        
        ans *= p
        ans %= MOD

    p = p**2 % MOD
    
    
print(ans)



