def heapify(arr, n, i):
    largest = i  # 父節點索引值
    left = 2 * i + 1  # 左子節點index值
    right = 2 * i + 2  # 右子節點index值

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    # build max-heap，由下往上調整成最大堆積
    # 對於一個具有 n 個節點的完全二叉樹，最後一個非葉子節點的索引為 n//2-1
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # 每次將最大的跟最小的互換，並縮小陣列長度，繼續調整為最大堆積，一直重複直到排序完成
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))

    heap_sort(arr)

    print(" ".join(map(str, arr)))

# Sample Input 1
# 20
# 1 3 43 38 23 25 34 34 33 43 17 30 12 4 17 48 33 16 43 22

# Sample Output 1
# 1 3 4 12 16 17 17 22 23 25 30 33 33 34 34 38 43 43 43 48

# Sample Input 2
# 10
# 991 524 769 239 473 113 252 183 362 267

# Sample Output 2
# 113 183 239 252 267 362 473 524 769 991
