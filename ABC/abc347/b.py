S = input()

ans_set = set()

for i in range(len(S)):
    for j in range(i+1, len(S)+1):
        ans_set.add(S[i:j])
        
print(len(ans_set))





































