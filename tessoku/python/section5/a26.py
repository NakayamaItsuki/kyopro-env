
N = int(input())

Xs = []
for i in range(N):
    Xs.append(int(input()))

def is_prime(n):
    
    flag = True
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            flag = False
            break

    return flag


for X in Xs:
    
    if is_prime(X):
        print("Yes")
        
    else:
        print("No")