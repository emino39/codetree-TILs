n = int(input())
prices = list(map(int, input().split()))

start = prices[0]
max_diff = 0

for i in range(1, n):
    if start < prices[i]:
        max_diff = max(max_diff, prices[i] - start)
    elif start > prices[i]:
        start = prices[i]

print(max_diff)