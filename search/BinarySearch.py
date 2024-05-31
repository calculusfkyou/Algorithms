def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return "not found"


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    while 1:
        target = int(input())
        if target == 0:
            break
        print(binary_search(arr, target))

# Sample Input1
# 10
# 2 4 6 8 9 10 13 23 25 30
# 4
# 7
# 13
# 25
# 32
# 0

# Sample Output1
# 1
# not found
# 6
# 8
# not found


# Sample Input2
# 15
# 3 6 7 8 10 12 18 19 27 29 31 35 38 41 45
# 12
# 41
# 7
# 25
# 31
# 24
# 34
# 19
# 0

# Sample Output2
# 5
# 13
# 2
# not found
# 10
# not found
# not found
# 7


# Sample Input3
# 20
# 7 8 11 15 17 26 28 29 33 52 62 64 75 76 85 87 89 90 92 99
# 11
# 44
# 90
# 96
# 33
# 82
# 99
# 74
# 85
# 41
# 0

# Sample Output3
# 2
# not found
# 17
# not found
# 8
# not found
# 19
# not found
# 14
# not found
