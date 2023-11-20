n, m = map(int, input().split())
jewels = []

for _ in range(n):
    w, v = map(int, input().split())
    jewels.append((w, v, v/w))

jewels = sorted(jewels, key=lambda x: x[2], reverse=True)
value = 0 # 가방 속 총 가치

for jewel in jewels:
    if m == 0:
        break
    
    # 가방 남은 무게가 현재 보석보다 클 때
    if m >= jewel[0]:
        value += jewel[1]
        m -= jewel[0]
    else:
        tmp = jewel[1] * m / jewel[0]
        value += tmp
        m -= m

print(f'{value:.3f}')