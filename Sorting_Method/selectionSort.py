def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n): # 往後找最小
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i] # 最小的移到前面


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))

    selection_sort(arr)

    print(" ".join(map(str, arr)))

# Sample Input 1
# 20
# 1 3 43 38 23 25 34 34 33 43 17 30 12 4 17 48 33 16 43 22

# Sample Output 1
# 1 3 4 12 16 17 17 22 23 25 30 33 33 34 34 38 43 43 43 48

# Sample Input 2
# 20
# 72 33 96 99 71 3 15 18 19 57 96 20 43 18 48 20 90 83 8 92

# Sample Output 2
# 3 8 15 18 18 19 20 20 33 43 48 57 71 72 83 90 92 96 96 99
