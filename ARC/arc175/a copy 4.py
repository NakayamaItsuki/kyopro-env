MOD = 998244353

def dfs(index, spoons, handedness):
    if index == N:
        return 1 if all(s == 0 for s in spoons) else 0

    # 現在の人の番号
    person = P[index] - 1
    left = person
    right = (person + 1) % N

    # スプーンが既に取られている場合は次へ
    if spoons[left] == 0 and spoons[right] == 0:
        return 0

    if handedness[person] != '?':
        # 利き手が決まっている場合、その手のスプーンを取る
        if handedness[person] == 'L' and spoons[left] == 1:
            spoons[left] = 0
        elif handedness[person] == 'R' and spoons[right] == 1:
            spoons[right] = 0
        return dfs(index + 1, spoons, handedness)
    else:
        # '?' の場合、両方の可能性を試す
        spoons_copy = spoons.copy()
        if spoons[left] == 1:
            spoons[left] = 0
            res_left = dfs(index + 1, spoons, handedness)
        else:
            res_left = 0

        if spoons_copy[right] == 1:
            spoons_copy[right] = 0
            res_right = dfs(index + 1, spoons_copy, handedness)
        else:
            res_right = 0

        return (res_left + res_right) % MOD

# 入力
N = int(input().strip())
P = list(map(int, input().strip().split()))
S = input().strip()

# 全スプーンが存在する初期状態
spoons = [1] * N

# 結果を計算
result = dfs(0, spoons, S)
print(result)
