n, s = map(int, input().split())
arr = [0] + list(map(int, input().split()))

ans = n + 2

sum_value = 0
j = 0
for i in range(1, n+1):
    while j + 1 <= n and sum_value < s:
        sum_value += arr[j + 1]
        j += 1

    if sum_value < s:
        break

    ans = min(ans, j - i + 1)

    sum_value -= arr[i]

if ans == n + 2:
    print(-1)
else:
    print(ans)