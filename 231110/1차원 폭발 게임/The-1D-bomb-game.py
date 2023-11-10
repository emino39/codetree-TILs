N, M = map(int, input().split())
arr = [0] * N

# arr 생성
for n in range(N):
    arr[N-n-1] = int(input())

if M == 1:
    print(0)
else:
    while True:
        flag = 0

        if len(arr) < M:
            break
        
        temp = [] # 새 arr
        t = []

        for i in range(len(arr)):
            if t == []:
                t = [arr[i]]
            else:
                if t[-1] == arr[i]:
                    t.append(arr[i])
                    if i == len(arr) -1:
                        if len(t) >= M:
                            flag = 1
                            t = []
                    # else:
                    #     t.append(arr[i])
                else:
                    if len(t) >= M:
                        flag = 1
                        if i == len(arr)-1:
                            temp += [arr[i]]
                            t = []
                        else:
                            t = [arr[i]]

                    else:
                        temp += t
                        t = [arr[i]]
        
        if t:
            temp += t
        
        arr = temp

        if not flag:
            break
        
    print(len(arr))

    for j in range(len(arr)-1, -1, -1):
        print(arr[j])