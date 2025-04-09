T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    lis = list(map(int, input().split()))
    mx = 0
    mn = 10000 * N
    sm = 0
    for i in range(N-M+1):
        sm = sum(lis[i:i+M])
        if sm < mn:
            mn = sm
        if sm > mx:
            mx = sm
    print(f'#{test_case}', mx-mn)