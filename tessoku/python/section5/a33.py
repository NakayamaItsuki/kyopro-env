
N = int(input())

As = list(map(int, input().split()))

flag = 0

for i in range(N):

    flag = flag ^ As[i]

if flag == 0:
    print("Second")
    
else:
    print("First")





