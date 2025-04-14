#먼저 끝나는 작업 우선
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr.sort(key = lambda x : x[1])
    last = cnt = 0
    for s, e in arr:
        if last <= s:
            cnt += 1
            last = e
    print(f'#{test_case}', cnt)