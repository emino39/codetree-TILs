n = int(input())
arr = list(map(int, input().split()))
cost = 0

while True:
    if len(arr) < 2:
        break
    
    arr = sorted(arr)

    n1 = arr.pop(0)
    n2 = arr.pop(0)

    cost += (n1 + n2)
    arr.append(n1 + n2)

print(cost)