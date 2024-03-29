def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
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
    num_digits = len(str(max_value))  # Get the number of digits in the maximum value

    # Iterate through each digit position from least significant to most significant
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
        print(" ".join(map(str, arr)))
