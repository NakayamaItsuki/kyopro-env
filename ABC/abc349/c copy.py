
S = input()
T = input().lower()

from collections import Counter

counter = Counter(S)

# print(counter)


flag = True

if T[-1] == 'x':
    
    if counter[T[0]] == 0:
        flag = False

    else :
        counter[T[0]] -= 1
    
    if counter[T[1]] == 0:
        flag = False
        
    else:
        counter[T[1]] -= 1

else:
    
    if counter[T[0]] == 0:
        flag = False
        
    else:
        counter[T[0]] -= 1
        
    
    if counter[T[1]] == 0:
        flag = False
    
    else:
        counter[T[1]] -= 1
    
    
    if counter[T[2]] == 0:
        flag = False
    
    else:
        counter[T[2]] -= 1

# print(counter)

if flag:
    print('Yes')
    
else:
    print('No')


