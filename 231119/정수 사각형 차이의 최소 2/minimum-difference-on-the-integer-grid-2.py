n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[(0, 999)] * n for _ in range(n)]
dp[0][0] = (arr[0][0], arr[0][0])

# 오른쪽
for j in range(1, n):
    max_n, min_n = dp[0][j-1]
    new_max = max(max_n, arr[0][j])
    new_min = min(min_n, arr[0][j])

    dp[0][j] = (new_max, new_min)

# 아래
for i in range(1, n):
    max_n, min_n = dp[i-1][0]
    new_max = max(max_n, arr[i][0])
    new_min = min(min_n, arr[i][0])

    dp[i][0] = (new_max, new_min)

# 대각선
for i in range(1, n):
    for j in range(1, n):
        # from up
        tmp1 = (max(dp[i-1][j][0], arr[i][j]), min(dp[i-1][j][1], arr[i][j]))
        tmp2 = (max(dp[i][j-1][0], arr[i][j]), min(dp[i][j-1][1], arr[i][j]))

        diff1 = abs(tmp1[0] - tmp1[1])
        diff2 = abs(tmp2[0] - tmp2[1])

        if diff1 < diff2:
            dp[i][j] = tmp1
        elif diff1 == diff2:
            if tmp1[0] > tmp2[0]:
                dp[i][j] = tmp2
            else:
                dp[i][j] = tmp1
        else:
            dp[i][j] = tmp2

# print(dp)
print(abs(dp[n-1][n-1][0] - dp[n-1][n-1][1]))