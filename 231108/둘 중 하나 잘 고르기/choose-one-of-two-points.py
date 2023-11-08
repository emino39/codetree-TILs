N = int(input())
red, blue = [0], [0]

for n in range(2*N):
    r, b = map(int, input().split())
    red.append(r)
    blue.append(b)

dp_b = [[-1] * (2 * N + 1) for _ in range(2 * N + 1)]
dp_b[0][0] = 0
dp_r = [[-1] * (2 * N + 1) for _ in range(2 * N + 1)]
dp_r[0][0] = 0

# 빨강을 선택하지 않는 경우는 파랑을 선택하는 경우로 간주
for i in range(1, 2 * N + 1):
    dp_b[i][0] = dp_b[i-1][0]
    dp_r[i][0] = dp_r[i-1][0]

    for j in range(1, i+1):
        dp_b[i][j] = max(dp_b[i-1][j] + red[i], dp_b[i-1][j-1] + blue[i])
        dp_r[i][j] = max(dp_r[i-1][j] + blue[i], dp_r[i-1][j-1] + red[i])

print(max(dp_b[2*N][N], dp_r[2*N][N]))