
S = input()

from collections import Counter
from collections import defaultdict

c = Counter(S)

flag = True

# print(c)

dict = defaultdict(int)

for v in c.values():
    dict[v] += 1

# print(dict)

for v in dict.values():
    if v != 2:
        flag = False
        break

if flag:
    print('Yes')
    
else:
    print('No')













