
N, K = map(int, input().split())

Cs, Vs = [], []

for _ in range(N):
    C, V = map(int, input().split())
    Cs.append(C)
    Vs.append(V)



# 隣合っている数をカウントする

cnt = 0

for i in range(N - 1): # 最後の要素は考えなくていい
    if Cs[i] == Cs[i + 1]:
        cnt += 1

# print(cnt)

# 隣あっているところが3つ以上ある場合は，不可能
if cnt > K:
    print(-1)
    exit()
    

# デバッグ
# print(100)


# 隣合っている場所を記憶しておく
# ただし，スタート側を記憶する

same_color_list = []
not_same_color_list = []

for i in range(N):
    
    if i!=N-1 and Cs[i] == Cs[i + 1]:
        same_color_list.append(i)

    elif i != 0 and Cs[i] == Cs[i - 1]:
        same_color_list.append(i)
        
    else:
        not_same_color_list.append(i)

# print(same_color_list)
# print(not_same_color_list)


# 隣合っている場所が無ければ，最小のK個を取り除けば良い
# 隣合っている場所が1つあれば，最小のK-1個と，same_color_listの中の最小の値を取り除けば良い
# 以下，同様．

# ans = 0
ans = sum(Vs)

# print(ans)

# 隣合っていないもののうち，valueが小さい順にK-cnt個取り除く

not_same_color_value = [Vs[i] for i in not_same_color_list]

not_same_color_value.sort()

ans -= sum(not_same_color_value[:K - cnt])

# print(ans)

# まず，隣合っているもののうち，valueが小さい順にcnt個取り除く

same_color_value = [Vs[i] for i in same_color_list]

same_color_value.sort()

ans -= sum(same_color_value[:cnt])

print(ans)

