n = int(input())
cnt = 0

flag = 0
while True:
    if n == 0:
        break

    if n == 1:
        flag = 1
        break
    
    if n >= 5:
        tmp = n % 5
        
        # 5 나누기
        if tmp % 2 == 0:
            cnt += (n // 5)
            n = n % 5
        else:
            cnt += (n // 5) - 1
            n = (n % 5) + 5
        
        # 2 나누기
        cnt += (n // 2)
        n = n % 2
        
    else:
        cnt += (n // 2)
        n = n % 2

if flag:
    print(-1)
else:
    print(cnt)