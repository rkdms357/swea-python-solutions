def bfs(s, e):
    q = []
    v = [1000000] * (N+1)
    q.append(s)
    v[s] = 0
    while q:
        c = q.pop(0)
        for (n, w) in adj[c]:
            if v[n] > v[c] + w:
                q.append(n)
                v[n] = v[c] + w
    return v[N]
T = int(input())
for test_case in range(1, T+1):
    N, E = map(int, input().split())
    adj = [[] for _ in range(N+1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        adj[s].append((e, w))
    ans = bfs(0, N)
    print(f'#{test_case}', ans)