def is_range(p, q):
    if 0 <= p < N and 0 <= q < N:
        return True
    return False

def change_dir(di):
    if di == 'U':
        return 'D'
    elif di == 'D':
        return 'U'
    elif di == 'L':
        return 'R'
    else:
        return 'L'

def next_position(a, b, c):
    if c == 'U':
        return (a-1, b)
    elif c == 'D':
        return (a+1, b)
    elif c == 'L':
        return (a, b-1)
    else:
        return (a, b+1)
    

T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    arr = [[0] * N for _ in range(N)]
    beads = dict()

    for m in range(M):
        x, y, d = map(str, input().split())
        x, y = int(x) - 1, int(y) - 1

        beads[m + 1] = (x, y, d)

        arr[x][y] = (m + 1)
    
    repeat = 0
    while True:
        if repeat > N * N:
            break
        
        repeat += 1

        new_arr = [[0] * N for _ in range(N)]
        
        # 사라질 구슬
        remove = []
        
        for i in range(N):
            for j in range(N):
                if arr[i][j] != 0:
                    x, y, d = beads[arr[i][j]]

                    nx, ny = next_position(x, y, d)

                    if is_range(nx, ny):
                        if new_arr[nx][ny] == 0:
                            new_arr[nx][ny] = arr[i][j]
                            beads[arr[i][j]] = (nx, ny, d)
                        else:
                            remove.append(arr[i][j])
                            if new_arr[nx][ny] not in remove:
                                remove.append(new_arr[nx][ny])
                    else:
                        beads[arr[i][j]] = (x, y, change_dir(d))
                        new_arr[x][y] = arr[i][j]

        # for bead in beads.keys():
        #     x, y, d = beads[bead]

        #     nx, ny = next_position(x, y, d)

        #     if is_range(nx, ny):
        #         if new_arr[x][y] == 0:
        #             new_arr[x][y] = bead
        #         else:
        #             remove.append(bead)
        #             if new_arr[x][y] not in remove:
        #                 remove.append(new_arr[x][y])
            
        #     else:
        #         beads[bead] = (x, y, change_dir(d))
        #         new_arr[x][y] = bead
        
        for rem in remove:
            p1, q1, d1 = beads[rem]
            new_arr[p1][q1] = 0
            del beads[rem]
        
        arr = new_arr
        
    print(len(beads.keys()))