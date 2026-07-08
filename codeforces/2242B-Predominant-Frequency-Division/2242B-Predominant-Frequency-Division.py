INF = 1000000007

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    pref1 = [0] * (n + 1)
    pref2 = [0] * (n + 1)
    for i in range(n):
        pref1[i + 1] = pref1[i] + (1 if a[i] == 1 else -1)
        pref2[i + 1] = pref2[i] + (-1 if a[i] == 3 else 1)

    mn = INF
    found = False
    for i in range(1, n):
        if pref2[i] - mn >= 0:
            print("YES")
            found = True
            break
        if pref1[i] >= 0:
            mn = min(mn, pref2[i])

    if not found:
        print("NO")