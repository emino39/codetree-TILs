def is_range(p, q):
    if 0 <= p < n and 0 <= q < n:
        return True
    return False

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, r, c = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
r -= 1
c -= 1

visited[r][c] = 1
# nums = [arr[r][c]]
print(arr[r][c], end=" ")

while True:
    flag = 0

    for i in range(4):
        nr = r + dx[i]
        nc = c + dy[i]

        if is_range(nr, nc) and not visited[nr][nc] and arr[nr][nc] > arr[r][c]:
            flag = 1
            r, c = nr, nc
            # nums.append(arr[nr][nc])
            print(arr[nr][nc], end=" ")
            break
    
    if not flag:
        break

# print(*nums)