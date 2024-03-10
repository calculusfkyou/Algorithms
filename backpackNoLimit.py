# 背包問題，各價位的硬幣數量不限，給予目標金額，求出有多少組合
coins = list(map(int, input().split()))
amount = int(input())
dp = [0 for i in range(amount + 1)]
dp[0] = 1
for i in coins:
    for j in range(i, amount + 1):
        dp[j] += dp[j - i]
print(dp[amount])
