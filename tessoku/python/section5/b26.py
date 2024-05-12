
N = int(input())

# エラストテネスのふるい

Deleted = [False] * (N+1) # 2~Nまでの数を削除したかどうか

for i in range(2, int(N**0.5)+1): # √Nまで調べればOK
    
    # 削除済み
    if Deleted[i] == True:
        continue
    
    # 削除済みでなければ，その倍数を削除
    for j in range(i*2, N+1, i):
        Deleted[j] = True

for i in range(2, N+1):
    if Deleted[i]==False:
        print(i)






