arr = [list(map(int, input().split())) for _ in range(4)]
direction = input()

temp = [[0] * 4 for _ in range(4)]

if direction == 'L':
    for i in range(4):
        tmp = []
        for j in range(4):
            if arr[i][j] != 0:
                tmp.append(arr[i][j])
    
        start = 0
        t = 0
        while tmp:
            s = tmp.pop(0)
            if start == 0:
                start = s
                if tmp == []:
                    temp[i][t] = s
            else:
                if start == s:
                    temp[i][t] = s * 2
                    start = 0
                    t += 1
                else:
                    temp[i][t] = start
                    start = s
                    t += 1

                    if tmp == []:
                        temp[i][t] = s

elif direction == 'R':
    for i in range(4):
        tmp = []
        for j in range(3, -1, -1):
            if arr[i][j] != 0:
                tmp.append(arr[i][j])
        
        start = 0
        t = 3
        while tmp:
            s = tmp.pop(0)
            if start == 0:
                start = s
                if tmp == []:
                    temp[i][t] = s
            else:
                if start == s:
                    temp[i][t] = s * 2
                    start = 0
                    t -= 1
                else:
                    temp[i][t] = start
                    start = s
                    t -= 1

                    if tmp == []:
                        temp[i][t] = s

elif direction == 'U':
    for j in range(4):
        tmp = []
        for i in range(4):
            if arr[i][j] != 0:
                tmp.append(arr[i][j])
            
        start = 0
        t = 0
        while tmp:
            s = tmp.pop(0)
            if start == 0:
                start = s
                if tmp == []:
                    temp[t][j] = s
            else:
                if start == s:
                    temp[t][j] = s * 2
                    start = 0
                    t += 1
                else:
                    temp[t][j] = start
                    start = s
                    t += 1

                    if tmp == []:
                        temp[t][j] = s
else:
    for j in range(4):
        tmp = []
        for i in range(3, -1, -1):
            if arr[i][j] != 0:
                tmp.append(arr[i][j])
        
        start = 0
        t = 3
        while tmp:
            s = tmp.pop(0)
            if start == 0:
                start = s
                if tmp == []:
                    temp[t][j] = s
            else:
                if start == s:
                    temp[t][j] = s * 2
                    start = 0
                    t -= 1
                else:
                    temp[t][j] = start
                    start = s
                    t -= 1

                    if tmp == []:
                        temp[t][j] = s

for tt in temp:
    print(*tt)