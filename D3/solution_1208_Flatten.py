for test_case in range(1, 11):
    d = int(input())
    lis = list(map(int, input().split()))
    for i in range(d):
        lis.sort()
        lis[0] += 1
        lis[-1] -= 1
    print(f'#{test_case}', max(lis)-min(lis))