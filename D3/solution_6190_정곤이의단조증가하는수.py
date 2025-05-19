def solve(n):
    n = list(map(int, str(n)))
    for i in range(1, len(n)):
        if n[i] >= n[i-1]:
            continue
        else:
            return False
    return True
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    ans = []
    for i in range(N-1):
        for j in range(i+1, N):
            if solve(lst[i] * lst[j]):
                ans.append(lst[i] * lst[j])
    if ans:
        print(f'#{test_case}', max(ans))
    else:
        print(f'#{test_case}', -1)