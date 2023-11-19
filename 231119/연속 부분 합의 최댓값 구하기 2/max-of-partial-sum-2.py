n = int(input())
arr = list(map(int, input().split()))
total = arr[0]
max_total = total

for i in range(1, n):
    if total + arr[i] < arr[i]:
        total = arr[i]
        max_total = max(max_total, total)

    else:
        if total + arr[i] < 0:
            max_total = max(max_total, total)
            total = arr[i]
        else:
            total += arr[i]
            max_total = max(max_total, total)

print(max_total)