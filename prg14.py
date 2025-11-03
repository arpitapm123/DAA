def obst(keys, freq):
    n = len(keys)
    dp = [[0] * n for i in range(n)]

    for i in range(n):
        dp[i][i] = freq[i]

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = 10 ** 9
            s = sum(freq[i:j + 1])

            for r in range(i, j + 1):
                left = dp[i][r - 1] if r > i else 0
                right = dp[r + 1][j] if r < j else 0
                dp[i][j] = min(dp[i][j], left + right + s)

    return dp[0][n - 1]
keys = list(map(int, input("Keys: ").split()))
freq = list(map(int, input("Freq: ").split()))

print("Optimal BST cost:", obst(keys, freq))