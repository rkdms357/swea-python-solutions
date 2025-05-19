T = 10
for test_case in range(1, T+1):
    N, st = input().split()
    ans = []
    for i in st:
        if not ans or ans[-1] != i:
            ans.append(i)
        else:
            ans.pop()
    print(f'#{test_case}', ''.join(ans))