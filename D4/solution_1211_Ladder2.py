T, N = 10, 100
for test_case in range(1, T+1):
    input()
    arr = [[0] + list(map(int, input().split())) + [0] for _ in range(N)]
    mn = 100*100
    for sj in range(1, N+1):
        if arr[0][sj] == 0:
            continue
        cj = sj
        ci = dr = cnt = 0
        while ci < 99:
            cnt += 1
            if dr == 0: # 아래
                ci += 1
                if arr[ci][cj-1] == 1:
                    dr = -1
                elif arr[ci][cj+1] == 1:
                    dr = 1
            else: # 좌/우
                cj += dr
                if arr[ci][cj+dr] == 0:
                    dr = 0
        if mn >= cnt:
            mn, ans = cnt, sj-1
    print(f'#{test_case}', ans)