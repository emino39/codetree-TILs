n = int(input())
arr = [0] * n

# 주어진 배열 채우기
for i in range(n-1, -1, -1):
    arr[i] = int(input())

for j in range(2):
    temp = []
    s, e = map(int, input().split())

    for k in range(s, e+1):
        arr[k * (-1)] = 0
    
    for l in range(len(arr)):
        if arr[l] != 0:
            temp.append(arr[l])
    
    arr = temp

print(len(arr))

for m in range(len(arr)-1, -1, -1):
    print(arr[m])