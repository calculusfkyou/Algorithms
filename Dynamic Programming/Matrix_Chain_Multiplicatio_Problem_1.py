def MatrixChainOrder(p):
    n = len(p) - 1
    m = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    s = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    for l in range(2, n + 1):
        for i in range(1, n - l + 2):
            j = i + l - 1
            m[i][j] = float("inf")
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k
    return m, s


def PrintOptimalSolution(s, i, j):
    if i == j:
        print(f"A{i}", end=" ")
    else:
        print("(", end=" ")
        PrintOptimalSolution(s, i, s[i][j])
        PrintOptimalSolution(s, s[i][j] + 1, j)
        print(")", end=" ")


if __name__ == "__main__":
    p = list(map(int, input().split()))
    n = len(p) - 1
    m, s = MatrixChainOrder(p)
    print(m[1][n])
    PrintOptimalSolution(s, 1, n)

# Sample Input 1
# 30 35 15 5 10 20 25

# Sample Output 1
# 15125  # 第一行為一個整數，表示獲得輸入的矩陣乘積所需的最少乘法次數
# ( ( A1 ( A2 A3 ) ) ( ( A4 A5 ) A6 ) )  # 第二行為矩陣鏈相乘的最佳括號方式，括號與不同矩陣之間皆須有空格隔開

# Sample Input 2
# 13 5 89 3 34

# Sample Output 2
# 2856
# ( ( A1 ( A2 A3 ) ) A4 )
