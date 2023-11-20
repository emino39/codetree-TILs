from functools import cmp_to_key

def compare(x, y):
    if (x + y) > (y + x):
        return -1

    if (x + y) < (y + x):
        return 1

    return 0

n = int(input())
arr = [input() for _ in range(n)]
max_num = 0

arr.sort(key=cmp_to_key(compare))
print("".join(arr))