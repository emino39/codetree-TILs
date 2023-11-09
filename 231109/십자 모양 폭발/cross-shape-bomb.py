def is_range(p, q):
    if 0 <= p < n and 0 <= q < n:
        return True
    return False

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split()) # 1씩 제거

# 제거하기
power = arr[r-1][c-1]
arr[r-1][c-1] = 0

for po in range(1, power):
    for i in range(4):
        nr = (r-1) + (dx[i] * po)
        nc = (c-1) + (dy[i] * po)

        if is_range(nr, nc):
            arr[nr][nc] = 0

# 숫자 옮기기
temp = [[0] * n for _ in range(n)]

for j in range(n):
    # temp 행 채우기 위한 변수
    t = n - 1
    for i in range(n-1, -1, -1):
        if arr[i][j] != 0:
            temp[t][j] = arr[i][j]
            t -= 1

for tmp in temp:
    print(*tmp)