def bfs(si, sj, ei, ej):
    q = []
    v = [[1000000] * N for _ in range(N)]
    q.append((si, sj))
    v[si][sj] = 0
    while q:
        ci, cj = q.pop(0)
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            if 0<=ni<N and 0<=nj<N and v[ni][nj] > v[ci][cj] + 1 + max(arr[ni][nj] - arr[ci][cj], 0):
                q.append((ni, nj))
                v[ni][nj] = v[ci][cj] + 1 + max(arr[ni][nj] - arr[ci][cj], 0) # 다음 위치 비용이 현재 위치 이동 비용보다 클때 중복 방문 허용
    return v[ei][ej]
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = bfs(0, 0, N-1, N-1)
    print(f'#{test_case}', ans)