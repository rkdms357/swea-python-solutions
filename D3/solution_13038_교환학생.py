T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    min_days = 100000 * 7
    for i in range(7):
        start = i
        cnt = 0
        days = 0
        while cnt < N:
            if lst[start%7] == 1:
                cnt += 1
            days += 1
            start += 1
        if days < min_days:
            min_days = days
    print(f'#{test_case}', min_days)