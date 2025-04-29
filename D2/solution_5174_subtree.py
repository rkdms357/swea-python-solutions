# N을 루트로 하는 서브트리의 노드개수 구하기
def preord(n):
    global ans
    if n:
        ans += 1
        preord(ch1[n])
        preord(ch2[n])
T = int(input())
for test_case in range(1, T+1):
    E, N = map(int, input().split())
    lst = list(map(int, input().split()))
    ch1 = [0] * (E+2)
    ch2 = [0] * (E+2)
    for i in range(0, len(lst), 2):
        p, c = lst[i], lst[i+1]
        if ch1[p] == 0:
            ch1[p] = c
        else:
            ch2[p] = c
    ans = 0
    preord(N)
    print(f'#{test_case}', ans)