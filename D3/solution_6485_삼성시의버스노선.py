T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    count = [0] * 5001
    for i in range(1, N+1):
        A, B = map(int, input().split())
        for j in range(A, B+1):
            count[j] += 1
    P = int(input())
    print(f'#{test_case}', end=' ')
    for k in range(1, P+1):
        C = int(input())
        print(count[C], end=' ')