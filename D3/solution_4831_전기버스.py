T = int(input())
for test_case in range(1, T+1):
    K, N, M = map(int, input().split())
    lis = [0] + list(map(int, input().split())) + [N] # 내가 탐색하려는 정류장! 출발점, 종점 추가
    cnt = start = 0 # 충전횟수, 출발점 or 내가 마지막으로 충전한 정류장
    for i in range(1, M+2): #  종점까지 더한 정류장 수 범위
        if lis[i] - start > K: # 갈 수 없으니, 이전 정류장에서 충전
            start = lis[i-1]
            cnt += 1
        if lis[i] - lis[i-1] > K: # 충전기 잘못 설치됐을 때
            cnt = 0
            break
    print(f'#{test_case}', cnt)
        