
A, B = map(int, input().split())

A_original, B_original = A, B

# A > B となるようにする
if A < B:
    A, B = B, A

# ユークリッドの互除法
while True:
    
    A, B = B, A % B # 最大公約数のペアが入れ替わっていく
    
    if A < B:
        A, B = B, A
    
    # 割り切れたら終了
    if B == 0:
        break
    
GCD = A

# A * B = GCD * LCM の関係がある
LCM = A_original * B_original // GCD

print(LCM)
