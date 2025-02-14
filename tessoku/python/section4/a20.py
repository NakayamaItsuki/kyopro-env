
S = input()
T = input()

dp = [ [ 0 ] * (len(T) + 1) for i in range(len(S) + 1) ]

for i in range(1,len(S)+1):
    for j in range(1,len(T)+1):
        
        # Sのi文字目とTのj文字目が一致する場合
        if S[i-1]==T[j-1]:
            
            # 左，上から移動する場合と，左上から赤い辺で移動する場合がある．
            dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]+1)

        # Sのi文字目とTのj文字目が一致しない場合
        else :
            
            # 左，上から移動する場合がある．
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[len(S)][len(T)])

"""
### numpyを使うバージョン．TLEになる ###
# →頻繁にリストにアクセスする場合はあんまり？

import numpy as np # →numpyは遅い

S = input()
T = input()

dp = np.zeros((len(S)+1, len(T)+1), dtype=int)

for i in range(1,len(S)+1):
    for j in range(1,len(T)+1):
        
        # Sのi文字目とTのj文字目が一致する場合
        if S[i-1]==T[j-1]:
            
            # 左，上から移動する場合と，左上から赤い辺で移動する場合がある．
            dp[i][j] = np.max([dp[i-1][j], dp[i][j-1], dp[i-1][j-1]+1])

        # Sのi文字目とTのj文字目が一致しない場合
        else :
            
            # 左，上から移動する場合がある．
            dp[i][j] = np.max([dp[i-1][j], dp[i][j-1]])

print(dp[len(S)][len(T)])
"""