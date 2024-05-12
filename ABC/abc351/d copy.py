
H, W = map(int, input().split())

arr = [list(input()) for _ in range(H)]

# print(arr)


from collections import deque

def max_freedom(H, W, grid):
    
    def in_bounds(x, y):
        return 0 <= x < H and 0 <= y < W

    def is_blocked(x, y):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if in_bounds(nx, ny) and grid[nx][ny] == '#':
                return True
        return False

    def bfs(x, y):
        queue = deque([(x, y)])
        visited = set([(x, y)])
        while queue:
            cx, cy = queue.popleft()
            
            if is_blocked(cx, cy):
                continue
            
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nx, ny = cx + dx, cy + dy
                
                # if grid[nx][ny] == '#':
                    # continue
                    
                # if in_bounds(nx, ny) and grid[nx][ny] == '#':
                #     continue
                
                if in_bounds(nx, ny) and (nx, ny) not in visited and grid[nx][ny] == '.':
                    visited.add((nx, ny))
                    queue.append((nx, ny))
                    # if not is_blocked(nx, ny):
                    #     visited.add((nx, ny))
                    #     queue.append((nx, ny))
                        
        
        # print(x,y)
        # print(visited)
        
        return len(visited)

    max_degree = 1
    for i in range(H):
        for j in range(W):
            if grid[i][j] == '.' and not is_blocked(i, j):
                max_degree = max(max_degree, bfs(i, j))

    return max_degree

# 入力例
# H, W = 3, 5
# grid = [
#     ".#...",
#     ".....",
#     ".#..#"
# ]

# 出力
# print(max_freedom(H, W, grid))
print(max_freedom(H, W, arr))  

