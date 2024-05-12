W, B = map(int, input().split())

# 0≤W,B≤100

# s = "wbwbwwbwbwbw" # wが7個、bが5個
s = [1,0,1,0,1,1,0,1,0,1,0,1] # 0,1で表現する

S = s * 15

# print(S)

for i in range(len(S)-(W+B)):
    if sum(S[i:i+W+B]) == W:
        print('Yes')
        exit()
    
print('No')





































