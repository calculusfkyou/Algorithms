def cut_rod(p, n):
    if n == 0:
        return 0
    q = float('-inf')
    for i in range(1, n + 1):
        q = max(q, p[i] + cut_rod(p, n - i))
    return q


# Example usage:
prices = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]  # Prices for rods of length 1 to 10
rod_length = 4  # Length of the rod
max_profit = cut_rod(prices, rod_length)
print("Maximum profit:", max_profit)
