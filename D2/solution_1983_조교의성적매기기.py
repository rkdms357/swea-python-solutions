grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    lst = [[0, 0]]
    idx, rank = 0, N//10
    for i in range(len(arr)):
        T = arr[i][0] * 0.35 + arr[i][1] * 0.45 + arr[i][2] * 0.2
        lst.append((i+1, T))
    lst.sort(key = lambda x:x[1], reverse = True)
    for j in range(1, len(lst)):
        if lst[j][0] == K:
            idx = j
            break
    ans = grade[idx//rank]
    print(f'#{test_case}', ans)