# bucket sort
import math


def insertion_sort(bucket):
    for i in range(1, len(bucket)):
        temp = bucket[i]
        j = i - 1
        while j >= 0 and temp < bucket[j]:
            bucket[j + 1] = bucket[j]
            j = j - 1
        bucket[j + 1] = temp


def bucket_sort(arr):
    b = [[] for i in range(len(arr))]  # 建立新陣列

    for i in arr:
        b[math.floor(i * len(arr))].append(i)  # 將元素放入對應的桶中

    temp = []
    for i in range(len(arr)):
        insertion_sort(b[i])
        temp.extend(b[i])

    return temp


if __name__ == "__main__":
    arr = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
    arr = bucket_sort(arr)
    print(*arr)
