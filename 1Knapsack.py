def knapsack_1_0(wes, vals, cap):
    dp = [0] * (cap + 1)

    for i in range(len(wes)):
        for w in range(cap, wes[i] - 1, -1):
            dp[w] = max(dp[w], vals[i] + dp[w - wes[i]])

    return dp[cap]


no_of_items = int(input("Enter no of elements: "))

weights = []
values = []

for i in range(no_of_items):
    k = int(input(f"Enter the weight of item {i+1}: "))
    l = int(input(f"Enter the value of item {i+1}: "))

    weights.append(k)
    values.append(l)

cap_max = int(input("Enter the Capacity: "))

print(knapsack_1_0(weights, values, cap_max))


