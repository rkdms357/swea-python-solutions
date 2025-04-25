T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    h = [0] * (N+1)
    last = 0
    for n in lst:
        last += 1
        h[last] = n
        c = last
        while c//2 and h[c] < h[c//2]:
            h[c], h[c//2] = h[c//2] , h[c]
            c //= 2
    ans = 0
    c = last//2
    while c:
        ans += h[c]
        c //= 2
    print(f'#{test_case}', ans)