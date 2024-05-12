
S = input()
T = input().lower()

from collections import Counter

# counter = Counter(S)

# print(counter)

flag = True


first_pos = S.find(T[0])

if first_pos == -1:
    flag = False

# print(first_pos)


S = S[first_pos+1:]
second_pos = S.find(T[1])

if second_pos == -1:
    flag = False
    
# print(first_pos+second_pos)


if T[-1] == 'x':
    
    if flag:
        print('Yes')
    
    else:
        print('No')

else :
    
    S = S[second_pos+1:]
    third_pos = S.find(T[2])
    
    # print(first_pos+second_pos+third_pos)
    
    if third_pos == -1:
        flag = False
        
    if flag:
        print('Yes')
    
    else:
        print('No')

