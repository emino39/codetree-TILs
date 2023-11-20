from heapq import heappush, heappop, heapify

n = int(input())
arr = list(map(int, input().split()))
heapify(arr)
cost = 0

while True:
    if len(arr) < 2:
        break

    n1 = heappop(arr)
    n2 = heappop(arr)

    cost += (n1 + n2)
    heappush(arr, n1+n2)

print(cost)