def is_prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


t = int(input())
for i in range(t):
    check = []
    ans = ""
    case = input()
    for j in case:
        if j in check:
            continue
        check.append(j)
        count = case.count(j)
        if is_prime(count):
            ans += j
    if ans == "":
        ans = "empty"
    print("Case %d: %s" % (i + 1, ans))
