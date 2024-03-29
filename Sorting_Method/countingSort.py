def counting_sort(arr):
    c = [0] * (max(arr) + 1)  # 初始化

    for num in arr:  # 算每個數字的數值出現次數
        c[num] += 1

    for i in range(1, max(arr) + 1):  # 轉換成累加陣列
        c[i] += c[i - 1]

    result = [0] * len(arr)  # 建立一個空陣列，用於寫入排序好的陣列

    for i in reversed(arr):  # 從原陣列由後往前排入result陣列
        result[c[i] - 1] = i
        c[i] -= 1

    return result


if __name__ == "__main__":
    while True:
        n = int(input())
        if n == 0:
            break
        arr = list(map(int, input().split()))
        sorted_arr = counting_sort(arr)
        print(" ".join(map(str, sorted_arr)) + " ")

# Sample Input 1
# 10
# 12 56 44 21 33 15 64 48 98 25
# 0

# Sample Output 1
# 12 15 21 25 33 44 48 56 64 98

# Sample Input 2
# 5
# 5 4 3 2 1
# 6
# 15 6 31 42 8 1
# 7
# 18 34 25 65 84 16 55
# 0

# Sample Output 2
# 1 2 3 4 5
# 1 6 8 15 31 42
# 16 18 25 34 55 65 84

# Sample Output 3
# 8
# 2 5 3 0 2 3 0 3
# 0

# Sample Output 3
# 0 0 2 2 3 3 3 5
