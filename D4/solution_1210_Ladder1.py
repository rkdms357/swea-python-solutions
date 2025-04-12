T, N = 10, 100
for test_case in range(1, T+1):
    input()
    arr = [[0] + list(map(int, input().split())) + [0] for _ in range(N)]
    ci = 99
    for j in range(1, N+1): # 사실 도착점이지만 출발점 찾기
        if arr[ci][j] == 2:
            cj = j
            break
    while ci > 0:
        arr[ci][cj] = 0
        if arr[ci][cj-1] == 1: # 왼쪽 체크
            cj -= 1
        elif arr[ci][cj+1] == 1: # 오른쪽 체크
            cj += 1
        else: # 위쪽 체크
            ci -= 1
    print(f'#{test_case}', cj-1)