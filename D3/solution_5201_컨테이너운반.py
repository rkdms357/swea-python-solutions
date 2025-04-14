T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    lis1 = list(map(int, input().split()))
    lis2 = list(map(int, input().split()))
    lis1.sort(reverse = True)
    lis2.sort(reverse = True)
    total = j = 0 # j는 lis2의 인덱스
    for i in lis1:
        if i <= lis2[j]:
            total += i
            j += 1
        if j == M:
            break
    print(f'#{test_case}', total)