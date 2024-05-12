
N = int(input())

Ts, As = [], []

for i in range(N):
    T, A = input().split()
    Ts.append(T)
    As.append(int(A))
    
ans = 0
for i in range(N):
    
    if Ts[i]=='+':
        ans += As[i]
    
    elif Ts[i]=='-':
        ans -= As[i]
        
    elif Ts[i]=='*':
        ans *= As[i]
    
    # print(ans % 10000)
    
    
    if ans < 0:
        ans += 10000
    
    ans %= 10000
    
    print(ans)
    




