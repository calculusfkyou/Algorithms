def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10  # 0 ~ 9

    for i in range(n):  # 從個位數開始算
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):  # 累加
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]


def radix_sort(arr):
    max_value = max(arr)
    exp = 1
    num_digits = len(str(max_value))  # 取得最大數字的長度

    # 從最低位數開始排序到最高位數
    for _ in range(num_digits):
        counting_sort(arr, exp)
        exp *= 10


if __name__ == "__main__":
    while True:
        n = int(input())
        if n == 0:
            break
        arr = list(map(int, input().split()))
        radix_sort(arr)
        print(" ".join(map(str, arr)) + " ")

# Sample Input 1:
# 10
# 991 524 769 239 473 113 252 183 362 267
# 0

# Sample Output 1:
# 113 183 239 252 267 362 473 524 769 991
