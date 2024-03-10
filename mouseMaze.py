def find_path(maze):
    N = len(maze)
    visited = [[False] * N for _ in range(N)]
    path = []

    def dfs(x, y, N):
        # if x < 0 or y < 0 or x > (N - 1) or y > (N - 1):  # 越界
        #     return False

        if x == N - 1 or y == N - 1:  # 到達邊緣
            path.append((x, y))
            return True

        if 0 <= x < N and 0 <= y < N and maze[x][y] == 0 and not visited[x][y]:
            visited[x][y] = True
            path.append((x, y))

            # 向右走
            if dfs(x, y + 1, N):
                return True
            # 向下走
            if dfs(x + 1, y, N):
                return True
            # 向左走
            if dfs(x, y - 1, N):
                return True
            # 向上走
            if dfs(x - 1, y, N):
                return True

            # 若四個方向都走不通，回溯
            path.pop()
            return False

        return False

    if dfs(0, 0, N):
        return path
    else:
        return [(0, 0)]  # 若無法找到路徑，回傳 (0, 0)


# 讀取輸入
N = int(input())
maze = [list(map(int, input().split())) for _ in range(N)]

# 呼叫函數並輸出結果
result = find_path(maze)
for point in result:
    print(point)
