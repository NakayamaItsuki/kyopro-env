
N = int(input())

As = list(map(int, input().split()))


K = 0
change_pair = []


for i in range(N-1):
    
    # print(As)
    # print(i)
    
    if As[i] != i+1:
        
        # スワップ
        tmp = As[i]
        As[i] = As[As[i]-1]
        As[tmp-1] = tmp
        
        K += 1
        # change_pair.append([i+1, tmp])
        
        if i+1 < tmp:
            change_pair.append([i+1, tmp])
        else:
            change_pair.append([tmp, i+1])
        
    
print(K)

for i in range(K):
    print(change_pair[i][0], change_pair[i][1])
    
        
# K = 0
# change_pair = []

# # バブルソート
# for i in range(N):
    
#     for j in range(N-1, i, -1):
        
#         if As[j] < As[j-1]:
            
#             As[j], As[j-1] = As[j-1], As[j]
            
#             K += 1
            
#             change_pair.append([j, j+1])

# print(K)

# for i in range(K):
#     print(change_pair[i][0], change_pair[i][1])












