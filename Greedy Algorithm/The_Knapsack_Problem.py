def knapsack(value, weight, capacity):
    n = len(value)
    ratio = [value[i] / weight[i] for i in range(n)]
    index = list(range(n))
    index.sort(key=lambda i: ratio[i], reverse=True)
    max_value = 0
    fractions = [0] * n
    for i in index:
        if weight[i] <= capacity:
            fractions[i] = 1
            max_value += value[i]
            capacity -= weight[i]
        else:
            fractions[i] = capacity / weight[i]
            max_value += value[i] * capacity / weight[i]
            break
    return max_value, fractions


if __name__ == "__main__":
    value = list(map(int, input().split()))
    weight = list(map(int, input().split()))
    capacity = int(input())
    maxValue, amounts = knapsack(value, weight, capacity)
    for i in range(len(amounts)):
        if amounts[i] == 0.0:
            amounts[i] = 0
    print(maxValue, end=", ")
    print(amounts)

# Input
"""
value
weight
capacity
"""

# Sample Input1
# 25 24 15
# 18 15 10
# 20

# Sample Output1
# 31.5, [0, 1, 0.5]


# Sample Input2
# 60 100 120
# 10 20 30
# 50

# Sample Output2
# 240.0, [1, 1, 0.6666666666666666]


# Sample Input3
# 10 20 30 40 50 60
# 10 20 30 40 50 60
# 10

# Sample Output3
# 10.0, [1, 0, 0, 0, 0, 0]
