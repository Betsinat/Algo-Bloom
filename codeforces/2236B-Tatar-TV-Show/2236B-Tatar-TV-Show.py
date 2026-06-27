t = int(input())
for _ in range(t):
    n ,k= map(int,input().split())
    s = input()
    sl = list(s)
    for i in range(n-k):
        if sl[i] == "1":
            sl[i] = "0"
            if sl[i+k] == "1":
             sl[i+k] = "0"
            else:
             sl[i+k] = "1"
    if "1" not in sl:
        print("YES")
    else:
        print("NO")