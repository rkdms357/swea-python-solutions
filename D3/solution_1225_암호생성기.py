T = 10
for test_case in range(1, T+1):
    input()
    lst = list(map(int, input().split()))
    n = 1
    while n:
        for i in range(1, 6):
            n = lst[0]-i
            if n <= 0:
                n = 0
                lst.append(n)
                lst.pop(0)
                break
            lst.append(n)
            lst.pop(0)
    print(f'#{test_case}', *lst)