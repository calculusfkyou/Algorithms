# 一維陣列儲存最佳方案的價格
def cut_rod(prices, n):
    if n == 0:
        return 0
    max_val = float('-inf')
    for i in range(1, n + 1):
        max_val = max(max_val, prices[i] + cut_rod(prices, n - i))
    return max_val


# 自上而下的動態規劃
def top_down_cut_rod(prices, n):  # 紀錄每個長度能夠得到的最大價格
    memo = [float('-inf')] * (n + 1)
    return top_down_cut_rod_aux(prices, n, memo)


def top_down_cut_rod_aux(prices, n, memo):  # 計算每個長度的最大價格
    if memo[n] >= 0:
        return memo[n]
    if n == 0:
        return 0
    max_val = float('-inf')
    for i in range(1, n + 1):
        max_val = max(max_val, prices[i] + top_down_cut_rod_aux(prices, n - i, memo))
    memo[n] = max_val
    return max_val


def extended_bottom_up_cut_rod(prices, n):  # 紀錄每個長度的最大價格和切割點
    memo = [0] * (n + 1)
    cuts = [0] * (n + 1)
    for j in range(1, n + 1):
        max_val = float('-inf')
        for i in range(1, j + 1):
            if max_val < prices[i] + memo[j - i]:
                max_val = prices[i] + memo[j - i]
                cuts[j] = i
        memo[j] = max_val
    return memo[n], cuts


if __name__ == "__main__":
    prices = list(map(int, input().split()))
    prices.insert(0, 0)  # 補上長度為0的價格
    rod_length = len(prices) - 1

    print(cut_rod(prices, rod_length))

    print(top_down_cut_rod(prices, rod_length))

    r, s = extended_bottom_up_cut_rod(prices, rod_length)
    print("(" + str(r) + ", " + str(s) + ")")

# Sample Input 1
# 6 10 12 15 20 23

# Sample Output 1
# 36
# 36
# (36, [0, 1, 1, 1, 1, 1, 1])


# Sample Input 2
# 1 5 8 9 10 17 17 20 24 30

# Sample Output 2
# 30
# 30
# (30, [0, 1, 2, 3, 2, 2, 6, 1, 2, 3, 10])
