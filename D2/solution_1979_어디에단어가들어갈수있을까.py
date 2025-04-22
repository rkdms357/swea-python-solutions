def solve(arr):
    ans1 = 0
    for lst in arr:
        cnt = 0
        for i in range(N+1):
            if lst[i] != 0:
                cnt += 1
            else:
                if cnt == K:
                    ans1 += 1
                cnt = 0
    return ans1
T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) + [0] for _ in range(N)] + [[0] * (N+1)] 
    arr_t = list(map(list, zip(*arr))) # 전치 행렬 후 리스트로 변환
    ans = solve(arr) + solve(arr_t)
    print(f'#{test_case}', ans)