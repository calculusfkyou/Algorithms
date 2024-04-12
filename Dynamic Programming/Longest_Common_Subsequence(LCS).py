def longest_common_subsequence(x, y):
    m = len(x)
    n = len(y)

    c = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    b = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(m + 1):
        c[i][0] = 0
    for i in range(n + 1):
        c[0][i] = 0

    # 從[1,1]開始，因為[0,0]已經初始化為0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
                b[i][j] = "↖"
            elif c[i - 1][j] >= c[i][j - 1]:
                c[i][j] = c[i - 1][j]
                b[i][j] = "↑"
            else:
                c[i][j] = c[i][j - 1]
                b[i][j] = "←"

    return c, b


def print_lcs(b, x, i, j):
    if i == 0 or j == 0:
        return
    if b[i][j] == "↖":
        print_lcs(b, x, i - 1, j - 1)
        print(x[i - 1], end="")
    elif b[i][j] == "↑":
        print_lcs(b, x, i - 1, j)
    else:
        print_lcs(b, x, i, j - 1)


if __name__ == "__main__":
    x = input().strip()
    y = input().strip()
    c, b = longest_common_subsequence(x, y)
    print_lcs(b, x, len(x), len(y))

# Sample Input 1
# ABCBDAB
# BDCABA
#
# Sample Output 1
# BCBA

# Sample Input 2
# bacad
# accbadcb
#
# Sample Output 2
# acad
