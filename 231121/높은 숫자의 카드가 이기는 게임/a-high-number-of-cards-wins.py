N = int(input())
a_card, b_card = [], []
num_check =[0] * (2 * N + 1)

for _ in range(N):
    t = int(input())
    num_check[t] = 1
    b_card.append(t)

for n in range(1, 2*N+1):
    if num_check[n] == 0:
        a_card.append(n)

b_card.sort()

cnt = 0
j = 0
for i in range(N):
    if a_card[i] > b_card[j]:
        cnt += 1
        j += 1

print(cnt)