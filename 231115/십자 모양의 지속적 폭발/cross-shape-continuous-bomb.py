def is_range(p, q):
    if 0 <= p < n and 0 <= q < n:
        return True
    return False

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(m):
    col = int(input()) - 1
    flag = 0

    for row in range(n):
        power = arr[row][col]

        if flag:
            break

        if power == 0:
            continue
        else:
            flag = 1
            # 폭탄 터뜨리기
            arr[row][col] = 0

            if power >= 2:
                for i in range(1, power):
                    for j in range(4):
                        nr = row + (dx[j] * i)
                        nc = col + (dy[j] * i)

                        if is_range(nr, nc) and arr[nr][nc] != 0:
                            arr[nr][nc] = 0
            
            # 폭탄 내리기
            temp = [[0] * n for _ in range(n)]

            for c in range(n):
                t = n-1
                for r in range(n-1, -1, -1):
                    if arr[r][c] != 0:
                        temp[t][c] = arr[r][c]
                        t -= 1
            
            # 배열 변경
            arr = temp

for ar in arr:
    print(*ar)