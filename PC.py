count = 0
def dfs(field, x, y, originalX, originalY):
    global count
    if 0 <= (y - 2) <= (originalY - 1) and field[x][y - 2] == 1:  # 左
        field[x][y] = 0
        field[x][y - 2] = 777
        count += 1
        dfs(field, x, y - 2, originalX, originalY)
    if 0 <= (y + 2) <= (originalY - 1) and field[x][y + 2] == 1:  # 右
        field[x][y] = 0
        field[x][y + 2] = 777
        count += 1
        dfs(field, x, y + 2, originalX, originalY)
    if 0 <= (x - 2) <= (originalX - 1) and field[x - 2][y]:  # 上
        field[x][y] = 0
        field[x - 2][y] = 777
        count += 1
        dfs(field, x - 2, y, originalX, originalY)
    if 0 <= (x + 2) <= (originalX - 1) and field[x + 2][y]:  # 下
        field[x][y] = 0
        field[x + 2][y] = 777
        count += 1
        dfs(field, x + 2, y, originalX, originalY)
    return count


if __name__ == "__main__":
    n, m = map(int, input().split())
    field = [[1 for i in range(m)] for j in range(n)]
    field[0][0] = 777  # 炮
    print(dfs(field, 0, 0, n, m))
