
S = input()


flag = True

if S[0] != '<' or S[-1] != '>':
    flag = False
    
for s in S[1:-1]:
    if s != '=':
        flag = False
        break
    
if flag:
    print("Yes")

else:
    print("No")



