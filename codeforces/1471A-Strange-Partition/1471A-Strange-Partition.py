from math import ceil
t = int(input())
for _ in range(t):
    n , x= map(int , input().split())
    _max = 0
    arr = list(map(int , input().split()))
    for i in range(n):
        _max += ceil(arr[i] / x)
    _min = ceil(sum(arr) / x )
    print(_min , _max)