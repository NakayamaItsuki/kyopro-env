
from collections import deque

H, W = map(int, input().split())
grid = [input().strip() for _ in range(H)]

def in_bounds(x, y):
    return 0 <= x < H and 0 <= y < W

def is_blocked(x, y, grid):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if in_bounds(nx, ny) and grid[nx][ny] == '#':
            return True
    return False

def bfs(x, y, grid, freedom):
    queue = deque([(x, y)])
    visited = set([(x, y)])
    count = 0
    while queue:
        cx, cy = queue.popleft()
        
        if is_blocked(cx, cy, grid):
            continue
        
        count += 1
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = cx + dx, cy + dy
            if in_bounds(nx, ny) and (nx, ny) not in visited and grid[nx][ny] == '.':
                visited.add((nx, ny))
                queue.append((nx, ny))
    for vx, vy in visited:
        freedom[vx][vy] = count
    return count

freedom = [[-1] * W for _ in range(H)]
max_degree = 0
for i in range(H):
    for j in range(W):
        if grid[i][j] == '.' and freedom[i][j] == -1:
            if not is_blocked(i, j, grid):
                max_degree = max(max_degree, bfs(i, j, grid, freedom))

print(max_degree)


# H, W = map(int, input().split())

# arr = [list(input()) for _ in range(H)]


# from collections import deque

# def max_freedom(H, W, grid):
    
#     def in_bounds(x, y):
#         return 0 <= x < H and 0 <= y < W

#     def is_blocked(x, y):
#         directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
#         for dx, dy in directions:
#             nx, ny = x + dx, y + dy
#             if in_bounds(nx, ny) and grid[nx][ny] == '#':
#                 return True
#         return False

#     def bfs(x, y):
#         queue = deque([(x, y)])
#         visited = set([(x, y)])
#         while queue:
#             cx, cy = queue.popleft()
            
#             if is_blocked(cx, cy):
#                 continue
            
#             for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
#                 nx, ny = cx + dx, cy + dy
                
#                 if in_bounds(nx, ny) and (nx, ny) not in visited and grid[nx][ny] == '.':
#                     visited.add((nx, ny))
#                     queue.append((nx, ny))
        
#         return len(visited)

#     max_degree = 1
#     for i in range(H):
#         for j in range(W):
#             if grid[i][j] == '.' and not is_blocked(i, j):
#                 max_degree = max(max_degree, bfs(i, j))

#     return max_degree


# print(max_freedom(H, W, arr))  


