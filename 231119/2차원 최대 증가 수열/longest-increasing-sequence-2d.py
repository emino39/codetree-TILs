n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1] * m for _ in range(n)]
dp[0][0] = 1

for i in range(n-1):
    for j in range(m-1):
        if dp[i][j] == -1:
            continue
        # arr[i][j]
        for k in range(i+1, n):
            for l in range(j+1, m):
                if arr[k][l] > arr[i][j]:
                    dp[k][l] = max(dp[k][l], dp[i][j] + 1)

print(max(map(max, dp)))