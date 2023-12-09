def is_range(p, q):
    if 0 <=p < n and 0 <= q < n:
        return True
    return False

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m, t= map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

count = [[0] * n for _ in range(n)]

for _ in range(m):
    r, c = map(int, input().split())
    count[r-1][c-1] += 1

for tt in range(t):
    next_count = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if count[i][j] != 0:
                ii, jj = -1, -1
                max_value = -1
                
                for k in range(4):
                    ni = i + dx[k]
                    nj = j + dy[k]

                    if is_range(ni, nj):
                        if arr[ni][nj] > max_value:
                            max_value = arr[ni][nj]
                            ii, jj = ni, nj

                if ii == -1 and jj == -1:
                    next_count[i][j] += 1
                else:
                    next_count[ii][jj] += 1
    
    for x in range(n):
        for y in range(n):
            if next_count[x][y] > 1:
                next_count[x][y] = 0
    
    count = next_count

print(sum(map(sum, count)))