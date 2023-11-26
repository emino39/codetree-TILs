N = int(input())
bombs = [tuple(map(int, input().split())) for _ in range(N)]
bombs = sorted(bombs, key=lambda x: (x[1], -x[0]))

t = 0
point = 0

for power, time in bombs:
    if time > t:
        point += power
        t += 1

print(point)