#S ~ E까지 누적 합 더하기
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    S = E = M = N // 2
    ans = 0
    for i in range(N):
        if i < M:
            for j in range(S, E+1):
                ans += arr[j][i]
            S -= 1
            E += 1
        else:
            for j in range(S, E+1):
                ans += arr[j][i]
            S += 1
            E -= 1
    print(f'#{test_case}', ans)