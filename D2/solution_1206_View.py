for test_case in range(1, 11):
    N = int(input())
    lis = list(map(int, input().split()))
    total = 0
    mx = 0
    for i in range(2, N-2):
        mx = lis[i-2]
        for j in range(i-1, i+3):
            if i == j:
                continue
            else:
                if mx < lis[j]:
                    mx = lis[j]
        if lis[i] > mx:
            total += lis[i] - mx
    print(f'#{test_case}', total)