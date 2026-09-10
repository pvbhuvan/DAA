coins = list(map(int, input("Enter coin denominations: ").split()))
amount = int(input("Enter amount: "))

# dp[i] = minimum number of coins needed to make amount i
dp = [float('inf')] * (amount + 1)

dp[0] = 0

for i in range(1, amount + 1):
    for coin in coins:
        if coin <= i:
            dp[i] = min(dp[i], dp[i - coin] + 1)

if dp[amount] == float('inf'):
    print("Amount cannot be formed")
else:
    print("Minimum number of coins:", dp[amount])