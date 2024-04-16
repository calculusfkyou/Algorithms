# v1
# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr
#
#     mid = len(arr) // 2
#     left_half = arr[:mid]
#     right_half = arr[mid:]
#
#     left_half = merge_sort(left_half)
#     right_half = merge_sort(right_half)
#
#     return merge(left_half, right_half)
#
#
# def merge(left, right):
#     result = []
#     i = j = 0
#
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#
#     result.extend(left[i:])
#     result.extend(right[j:])
#     return result
#
#
# if __name__ == "__main__":
#     n = int(input())
#     arr = list(map(int, input().split()))
#     sorted_arr = merge_sort(arr)
#     print(*sorted_arr)

# v2
def merge_sort(arr, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(arr, p, q)
        merge_sort(arr, q + 1, r)
        merge(arr, p, q, r)


# q = mid, p = right, r = left
def merge(arr, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = [0] * (n1 + 1)
    R = [0] * (n2 + 1)
    for i in range(n1):
        L[i] = arr[p + i]
    for j in range(n2):
        R[j] = arr[q + j + 1]
    L[n1] = float('inf')
    R[n2] = float('inf')
    i = j = 0
    for k in range(p, r + 1):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    merge_sort(arr, 0, n - 1)
    print(*arr)

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
