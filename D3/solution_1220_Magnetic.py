T = 10
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr_t = list(zip(*arr)) # 전치 행렬로 변환
    cnt = 0
    for lst in arr_t:
        prev = 0
        for n in lst:
            if n: # 0이 아닌경우
                if n == 2 and prev == 1:
                    cnt += 1
                prev = n
    print(f'#{test_case}', cnt)