T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    mx = -1
    for si in range(N-M+1):
        for sj in range(N-M+1):
            sm = 0
            for i in range(si, si+M):
                for j in range(sj, sj+M):
                    sm += arr[i][j]
                    if sm > mx:
                        mx = sm
    print(f'#{test_case}', mx)