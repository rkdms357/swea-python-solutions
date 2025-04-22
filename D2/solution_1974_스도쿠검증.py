def solve():
    for lst in arr: # 행 체크
        if len(set(lst)) != N:
            return 0
    arr1 = list(zip(*arr)) # 전치 행렬로 변환
    for lst in arr1: # 열 체크 (행과 동일)
        if len(set(lst)) != N:
            return 0
    for i in range(0, 9, 3): # 3 x 3 block 체크
        for j in range(0, 9, 3):
            lst = arr[i][j:j+3] + arr[i+1][j:j+3] + arr[i+2][j:j+3] # 체크해줄 리스트에 추가
            if len(set(lst)) != N:
                return 0
    return 1
T = int(input())
N = 9
for test_case in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = solve()
    print(f'#{test_case}', ans)