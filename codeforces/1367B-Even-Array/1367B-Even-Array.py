t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    a = 0
    b = 0
    for i in range(len(arr)):
        if arr[i] % 2 == 0 and i % 2 != 0:
            a += 1
        elif arr[i] % 2 != 0 and i % 2 == 0:
            b += 1
    if a == b:
        print(a)
    else:
        print(-1)