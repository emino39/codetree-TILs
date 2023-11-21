N = int(input())
b_card = [int(input()) for _ in range(N)]
a_card = []

for n in range(1, 2*N+1):
    if n not in b_card:
        a_card.append(n)

b_card.sort()

cnt = 0
j = 0
for i in range(N):
    if a_card[i] > b_card[j]:
        cnt += 1
        j += 1

print(cnt)