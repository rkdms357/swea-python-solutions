T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))[::-1] # 뒤쪽 부터 탐색 (리스트 슬라이싱)
    ans = mx = 0
    for n in lst:
        if mx < n:
            mx = n
        else:
            ans += mx-n
    print(f'#{test_case}', ans)