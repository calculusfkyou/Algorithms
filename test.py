while 1:
    n = int(input())
    if n == 0:
        break
    information = [list(map(int, input().split())) for i in range(n)]
    check = 1
    while len(information) > 0:
        temp = information[0][::-1]
        if temp in information:
            information.remove(temp)
            information.pop(0)
        else:
            check = 0
            break
    if check:
        print("YES")
    else:
        print("NO")