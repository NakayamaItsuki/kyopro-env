N = int(input())

flag = False

As = [int(i) for i in input().split()]

for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            sum = As[i] + As[j] + As[k]
            
            if sum == 1000:
                flag = True
                break

if flag:
    print("Yes")
else:
    print("No")

