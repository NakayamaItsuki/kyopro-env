

N = int(input())

As = list(map(int, input().split()))

Ans = [As[0]]

for i in range(1,N):
    
    if Ans[-1] != As[i]:
        Ans.append(As[i])
        
    else :
        Ans[-1] += 1
        
        # print(i)
        # print(Ans)
        
        j = len(Ans) - 1
        
        # print(Ans[j], Ans[j-1])
        
        while 0 < j and Ans[j] == Ans[j-1]:
            Ans.pop(j)
            Ans[-1] += 1
            
            # print(Ans)
            j -= 1

# print(Ans)

print(len(Ans))





