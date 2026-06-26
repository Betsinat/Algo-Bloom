t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    s = 0
    for i in range(n):
      for j in range(i + 1 , n):
        if arr[j]> arr[i]:
           arr[j] = arr[i]
           break
    for a in arr:
       s += a
    print(s)