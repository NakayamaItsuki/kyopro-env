N, K = map(int, input().split())

As= list(map(int, input().split()))

ans = 1

vacant = K

i = 0

# for i in range(N):
while True:
    
    if As[i] <= vacant:
        vacant -= As[i]
        i += 1
        
        if i == N:
            break
        
    else:
        ans += 1
        vacant = K
        
    # print(vacant, ans)
        
print(ans)

