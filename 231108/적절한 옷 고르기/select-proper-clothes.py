N, M = map(int, input().split())
cloths = dict()

for i in range(N):
    cloths[i] = tuple(map(int, input().split()))

dp = [[-1] * (M+1) for _ in range(N)]

# 1일차 입력
for n in range(N):
    if cloths[n][0] == 1:
        dp[n][1] = 0

# 2일차부터 입력
for m in range(2, M+1):
    for n in range(N):
        # 해당 일자가 옷 입을 수 있는 날인지 체크
        if cloths[n][0] <= m <= cloths[n][1]:
            for k in range(N):
                # 이전 날에 옷을 입었을 때
                if dp[k][m-1] != -1:
                    dp[n][m] = max(dp[n][m], dp[k][m-1] + abs(cloths[n][2] - cloths[k][2]))

max_value = -1
for l in range(N):
    max_value = max(max_value, dp[l][M])

# print(dp)
print(max_value)