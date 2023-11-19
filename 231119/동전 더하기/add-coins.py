n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
cnt = 0

for i in range(n-1, -1, -1):
    if k == 0:
        break
    
    if k < coins[i]:
        continue
    
    cnt += (k // coins[i])
    k = k % coins[i]

print(cnt)