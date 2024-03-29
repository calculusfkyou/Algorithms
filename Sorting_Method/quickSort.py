def partition(arr, low, high):  # 分割
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


if __name__ == "__main__":
    while 1:
        n = int(input())
        if n == 0:
            break
        arr = list(map(int, input().split()))

        quick_sort(arr, 0, n - 1)

        print(" ".join(map(str, arr)))

# Sample Input 1
# 10
# 12 56 44 21 33 15 64 48 98 25
# 0

# Sample Output 1
# 12 15 21 25 33 44 48 56 64 98


# Sample Input 2
# 20
# 72 33 96 99 71 3 15 18 19 57 96 20 43 18 48 20 90 83 8 92

# Sample Output 2
# 3 8 15 18 18 19 20 20 33 43 48 57 71 72 83 90 92 96 96 99
