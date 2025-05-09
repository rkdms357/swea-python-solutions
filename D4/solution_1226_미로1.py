def bfs(si, sj):
    q = []
    v = [[0] * N for _ in range(N)]
    q.append((si, sj))
    v[si][sj] = 1
    while q:
        ci, cj = q.pop(0)
        if arr[ci][cj] == 2:
            return 1
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<N and v[ni][nj] == 0 and arr[ni][nj] != 1:
                q.append((ni, nj))
                v[ni][nj] = v[ci][cj] + 1
    return 0
T, N = 10, 16
for test_case in range(1, T+1):
    input()
    arr = [list(map(int, input())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 3:
                si, sj = i, j
                break
    ans = bfs(si, sj)
    print(f'#{test_case}', ans)