N = int(input())
red, blue = [0], [0]

for n in range(2*N):
    r, b = map(int, input().split())
    red.append(r)
    blue.append(b)


dp = [[-1] * (2 * N + 1) for _ in range(2 * N + 1)]
dp[0][0] = 0

# 빨강을 선택하지 않는 경우는 파랑을 선택하는 경우로 간주
for i in range(1, 2 * N + 1):
    dp[i][0] = dp[i-1][0]

    for j in range(i+1):
        if j > 0:
            dp[i][j] = max(dp[i][j], dp[i-1][j-1] + red[i])
        if i - j > 0:
            dp[i][j] = max(dp[i][j], dp[i-1][j] + blue[i])

print(dp[2*N][N])