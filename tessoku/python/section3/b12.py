N = int(input())

def func(x: float) -> float:
    return x**3 + x

left = 0.0
right = N ** (1/3)

while left <= right:

    mid = (left + right) / 2
    
    # midの時の印刷枚数を計算
    output = func(mid)
    
    if output < N:
        left = mid
    elif abs(output - N) < 0.001:
        print(mid)
        
        # デバッグ
        # print(output, N, abs(output - N))
        
        break
    else:
        right = mid
    
