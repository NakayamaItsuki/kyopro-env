
N = int(input())

As, Cs = [], []

for i in range(N):
    A, C = map(int, input().split())
    As.append(A)
    Cs.append(C)
    
    
# 各色ごとに，最小値を格納して，最小値が最大の色を選ぶ

from collections import defaultdict

color_dict = defaultdict(lambda: 10**9)

for i in range(N):

    color_dict[Cs[i]] = min(color_dict[Cs[i]], As[i])


print(max(color_dict.values()))
      
# valueが最大のkeyを取得
# max_color = max(color_dict, key=color_dict.get)

# print(color_dict[max_color])

# print(color_dict)



