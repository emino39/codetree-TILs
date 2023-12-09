def is_range(p, q):
    if 0 <= p < n and 0 <= q < n:
        return True
    return False

dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

for mm in range(m):
    num = 1
    while True:
        if num > n * n:
            break

        flag = 0
        for i in range(n):
            if flag:
                break
            for j in range(n):
                if arr[i][j] == num:
                    x, y = i, j
                    flag = 1
                    break
        
        xx, yy = -1, -1
        max_value = -1
        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]

            if is_range(nx, ny):
                if arr[nx][ny] > max_value:
                    max_value = arr[nx][ny]
                    xx, yy = nx, ny
        
        # print(arr[x][y], arr[xx][yy])
        tmp = arr[x][y]
        arr[x][y] = arr[xx][yy]
        arr[xx][yy] = tmp

        num += 1

for ar in arr:
    print(*ar)