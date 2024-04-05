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
