def change_zero(p, q):
    # p: start, q: end
    for j in range(p, q+1):
        arr[j] = 0

def remove_zero():
    tmp = []

    for j in range(len(arr)):
        if arr[j] != 0:
            tmp.append(arr[j])
    
    return tmp

N, M = map(int, input().split())
arr = [0] * N

for n in range(N):
    arr[N-n-1] = int(input())

while True:
    cnt = 1 # 같은 숫자일 때 count (default 1)
    s, e = 0, 0 # 같은 숫자 인덱스 체크
    flag = 0

    if len(arr) < M:
        break

    for i in range(1, len(arr)):
        if arr[i] == arr[s]:
            cnt += 1
            e = i
            
        else:
            if cnt >= M:
                flag = 1
                change_zero(s, e)
            cnt = 1
            s, e = i, i

    if cnt >= M:
        if s <= e:
            change_zero(s, e)
            flag = 1

    if flag:
        arr = remove_zero()
    
    if not flag:
        break

print(len(arr))

for k in range(len(arr)-1, -1, -1):
    print(arr[k])