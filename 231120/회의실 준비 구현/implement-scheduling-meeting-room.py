n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]
arr = sorted(arr, key=lambda x: x[1])
cnt = 0
e = -1

for ar in arr:
    if ar[0] >= e:
        cnt += 1
        e = ar[1]

print(cnt)