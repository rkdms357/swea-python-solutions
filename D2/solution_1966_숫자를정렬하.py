T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    for i in range(N):
        mn = i
        for j in range(i+1, N):
            if lst[mn] > lst[j]:
                mn = j
        lst[i], lst[mn] = lst[mn], lst[i]
    print(f'#{test_case}', *lst)