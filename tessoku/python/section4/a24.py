
N, M = map(int, input().split())

As = [ None ] * (M+1)
for i in range(1, M+1):
	As[i] = list(map(int, input().split()))

# dp[i][S] := クーポン券iまで使って品物集合Sが買える時の，最小のクーポン枚数
dp = [ [ 10 ** 9 ] * (2 ** N) for i in range(M + 1) ]

# 動的計画法
dp[0][0] = 0
for i in range(1, M+1):
	for j in range(0, 2 ** N):
     
		already = [ None ] * (N+1)
		for k in range(1, N+1):
			if (j // (2 ** (k-1))) % 2 == 0: # 2のk-1乗で割り切れるなら，k番目の品物はまだ買っていない
				already[k-1] = 0
			else:
				already[k-1] = 1

        # 集合の整数表現v
		v = 0
		for k in range(1, N+1):
			if already[k-1] == 1 or As[i][k-1] == 1: # すでに買っているか，今回買うか
				v += (2 ** (k-1))

		# 遷移を行う
		dp[i][j] = min(dp[i][j], dp[i-1][j]) # クーポンiを使わない場合
		dp[i][v] = min(dp[i][v], dp[i-1][j] + 1) # クーポンiを使う場合

# 出力
if dp[M][2 ** N - 1] == 1000000000:
	print("-1")
else:
	print(dp[M][2 ** N - 1])



    