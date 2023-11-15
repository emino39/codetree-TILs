n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

flag = 0
row = 0
for i in range(1, n):
    if flag:
        break
    for j in range(k-1, k+m-1):
        if arr[i][j] == 1:
            row = i - 1
            flag = 1
            break

for l in range(k-1, k+m-1):
    arr[row][l] = 1

for ar in arr:
    print(*ar)