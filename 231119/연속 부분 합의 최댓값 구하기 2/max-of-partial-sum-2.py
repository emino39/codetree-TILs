import sys
sys.stdin = open('input.txt')

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
total = arr[0]
# max_total = (-1000) * n
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