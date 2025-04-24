# 중위 순회
def inord(n):
    global cnt # 전역 변수
    if n <= N:
        inord(n*2)
        lst[n] = cnt
        cnt += 1
        inord(n*2+1)
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    lst = [0] * (N+1)
    for i in range(1, N+1):
        lst[i] = i
    cnt = 1
    inord(1)
    print(f'#{test_case}', lst[1], lst[N//2])