

# 解説より．bool配列と深さ優先探索でグループ分けを行うらしい．
# https://atcoder.jp/contests/abc350/submissions/52521241
import sys
import pypyjit

sys.setrecursionlimit(10**6)
pypyjit.set_param("max_unroll_recursion=-1")

N, M = map(int, input().split())
g = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)
used = [False] * N


def dfs(u):
    used[u] = True
    res = 1
    for v in g[u]:
        if not used[v]:
            res += dfs(v)
    return res


ans = -M
for i in range(N):
    if not used[i]:
        s = dfs(i)
        ans += s * (s - 1) // 2
print(ans)





N, M = map(int, input().split())

# As , Bs = [], []

# for i in range(M):
    # A, B = map(int, input().split())
    
    # As.append(A-1)
    # Bs.append(B-1)

edges = [tuple(map(int, input().split())) for _ in range(M)]

# 全て1引く
for i in range(M):
    edges[i] = (edges[i][0]-1, edges[i][1]-1)


class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))

    def find(self, p):
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])  # path compression
        return self.parent[p]

    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP != rootQ:
            self.parent[rootQ] = rootP  # union the roots

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def components(self):
        # Create a dictionary of groups
        groups = {}
        for node in range(len(self.parent)):
            root = self.find(node)
            if root not in groups:
                groups[root] = []
            groups[root].append(node)
        return list(groups.values())


# Create a Union-Find instance with an arbitrary size
uf = UnionFind(N)  # We need 11 because our nodes start from 1 and go up to 10

# Add edges to the Union-Find structure
for (a, b) in edges:
    uf.union(a, b)

# Get the components
groups = uf.components()
# print("Groups:", groups)

sum = 0

for group in groups:
    n = len(group)
    sum += n * (n - 1) // 2

sum -= M

print(sum)





# # print(As)


# # set_list = []
# group

# # グループ間でエッジが無いようにグループに分ける
# # その後，n*(n-1)/2 - グループ内のエッジ数 を計算する

# for i in range(M):
    
    





# for i in range(M):

# class UnionFind:
#     def __init__(self, size):
#         self.parent = list(range(size))
#         self.rank = [1] * size
#         self.size = [1] * size

#     def find(self, p):
#         if self.parent[p] != p:
#             self.parent[p] = self.find(self.parent[p])  # パス圧縮
#         return self.parent[p]

#     def union(self, p, q):
#         rootP = self.find(p)
#         rootQ = self.find(q)
#         if rootP != rootQ:
#             # ランクに基づいた結合
#             if self.rank[rootP] > self.rank[rootQ]:
#                 self.parent[rootQ] = rootP
#                 self.size[rootP] += self.size[rootQ]
#             elif self.rank[rootP] < self.rank[rootQ]:
#                 self.parent[rootP] = rootQ
#                 self.size[rootQ] += self.size[rootP]
#             else:
#                 self.parent[rootQ] = rootP
#                 self.size[rootP] += self.size[rootQ]
#                 self.rank[rootP] += 1

#     def get_size(self, p):
#         rootP = self.find(p)
#         return self.size[rootP]

# def max_operations_correct(N, M, friendships):
#     uf = UnionFind(N)  # 0-indexed に調整するために N で初期化
#     edges_count = [0] * N
    
#     # エッジを追加し、連結成分を統合
#     for u, v in friendships:
#         uf.union(u - 1, v - 1)  # 1-indexed から 0-indexed に変換

#     # エッジをカウント
#     for u, v in friendships:
#         root_u = uf.find(u - 1)
#         root_v = uf.find(v - 1)
#         if root_u == root_v:
#             edges_count[root_u] += 1

#     # 連結成分の情報を集計
#     component_edges = {}
#     for i in range(N):
#         root = uf.find(i)
#         if root not in component_edges:
#             component_edges[root] = {
#             "size": 0,
#             "edge_count": 0
#             }
#         component_edges[root]["size"] += 1
#         component_edges[root]["edge_count"] = edges_count[root]

#     total_operations = 0
#     for info in component_edges.values():
#         n = info["size"]
#         actual_edges = info["edge_count"]
#         max_edges = n * (n - 1) // 2
#         operations = max_edges - actual_edges
#         total_operations += operations

#     return total_operations

# # 再度テストケースで試す


# # テストケース
# N = 4
# M = 3
# friendships = [(1, 2), (2, 3), (1, 4)]

# print(max_operations_correct(N, M, friendships))






