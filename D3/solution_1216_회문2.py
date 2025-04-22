def is_pal_idx(arr, leng):
    for lst in arr:
        for i in range(N-leng+1): # 모든 시작지점
            for j in range(leng//2): # 반만 검사
                if lst[i+j] != lst[i+leng-1-j]:
                    break # 다음 시작 위치로
            else:  # break 안 한 경우
                return True
    return False
T = 10
for test_case in range(1, T + 1):
    tc = input()
    N = 100
    arr1 = [input() for _ in range(N)]         
    arr2 = [''.join(x) for x in zip(*arr1)]
    for leng in range(N, 1, -1): # leng 길이의 회문을 찾으면 최대값
         if is_pal_idx(arr1, leng) or is_pal_idx(arr2, leng):
                break
    print(f'#{tc}', leng)