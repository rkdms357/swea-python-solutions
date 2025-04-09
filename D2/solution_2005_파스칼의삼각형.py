T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [[0] * (N+1) for _ in range(N+1)]
    for i in range(1, N+1):
        arr[i][1] = 1
        for j in range(2, N+1):
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
    print(f'#{test_case}')
    for k in range(1, N+1):
        print(*arr[k][1:k+1])