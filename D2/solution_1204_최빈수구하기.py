T = int(input())
for test_case in range(1, T+1):
    input()
    lst = list(map(int, input().split()))
    cnts = [0] * 1001
    ans = 0
    for i in range(len(lst)):
        cnts[lst[i]] += 1
    mx = max(cnts)
    for j in range(len(cnts)-1, -1, -1):
        if cnts[j] == mx:
            ans = j
            break
    print(f'#{test_case}', ans)