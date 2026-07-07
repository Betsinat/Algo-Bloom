t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a_sum = 0
    b_sum = 0
    possible = True
    for i in range(n):
        a_sum += a[i]
        b_sum += b[i]
        if a_sum > b_sum :
            possible = False
            break
    if possible:
        print ("YES")
    else:
        print("NO")