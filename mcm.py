n = int(input("Enter number of matrices: "))

print("Enter the dimensions:")
p = list(map(int, input().split()))



dp = [[0] * n for _ in range(n)]


for length in range(2, n):
    for i in range(1, n - length + 1):
        j = i + length - 1

        dp[i][j] = float('inf')

        for k in range(i, j):
            cost = (
                dp[i][k]
                + dp[k + 1][j]
                + p[i - 1] * p[k] * p[j]
            )

            dp[i][j] = min(dp[i][j], cost)

print("Minimum number of scalar multiplications:", dp[1][n - 1])