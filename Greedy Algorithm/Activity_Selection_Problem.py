def recursive_activity_selector(s, f, k, n):
    m = k + 1
    while m <= n and s[m] < f[k]:
        m += 1
    if m <= n:
        return [m] + recursive_activity_selector(s, f, m, n)
    else:
        return []


def greedy_acitivty_selector(s, f):
    n = len(s)
    A = []
    k = 0
    for m in range(1, n):
        if s[m] >= f[k]:
            A.append(m)
            k = m
    return A


if __name__ == "__main__":
    s = list(map(int, input().split()))
    f = list(map(int, input().split()))
    print(*recursive_activity_selector(s, f, 0, len(s) - 1), "")
    print(*greedy_acitivty_selector(s, f))

# Sample Input 1
# 0 1 2 3 3 2 1 9 1 5 9 6
# 0 4 5 6 7 8 9 10 11 12 13 14

# Sample Output 1
# 1 7
# 1 7


# Sample Input 2
# 0 2 3 4 8 9 9 0 17 3 20 39 4 26 31
# 0 4 7 8 11 11 15 16 20 26 39 41 43 44 45

# Sample Output 2
# 1 3 4 8 10 11
# 1 3 4 8 10 11
