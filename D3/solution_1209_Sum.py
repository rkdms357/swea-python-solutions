T = 10
N = 100
for test_case in range(1, T+1):
    input()
    arr = [list(map(int, input().split())) for _ in range(N)]
    dia_sm1, dia_sm2, mx = 0, 0, 0
    for i in range(N):
        row_sm, col_sm = 0, 0
        for j in range(N):
            row_sm += arr[i][j]
            col_sm += arr[j][i]
            mx = max(mx, row_sm, col_sm)
        dia_sm1 += arr[i][i]
        dia_sm2 += arr[i][N-1-i]
    mx = max(mx, dia_sm1, dia_sm2)
    print(f'#{test_case}', mx)