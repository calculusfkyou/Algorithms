n = int(input())
arr = list(map(int, input().split()))
for i in range(1, len(arr)):
    # key = arr[i]
    for j in range(i - 1, -1, -1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j + 1] = arr[j+1], arr[j]
print(*arr)

# Sample Input 1
# 10
# 20 8 10 2 14 4 3 15 17 16
#
# Sample Output 1
# 2 3 4 8 10 14 15 16 17 20

# Sample Input 2
# 20
# 72 33 96 99 71 3 15 18 19 57 96 20 43 18 48 20 90 83 8 92
#
# Sample Output 2
# 3 8 15 18 18 19 20 20 33 43 48 57 71 72 83 90 92 96 96 99