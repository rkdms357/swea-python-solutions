# 중위 순회
def inord(n):
    if n <= N:
        inord(n*2)
        ans.append(lst[n])
        inord(n*2+1)
    return 0
T = 10
for test_case in range(1, T+1):
    N = int(input())
    lst = [0] * (N+1)
    for _ in range(N):
        tlst = list(map(str, input().split()))
        idx = int(tlst[0])
        lst[idx] = tlst[1]
    ans = []
    inord(1)
    print(f'#{test_case}', "".join(ans))