T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    if N > M:
        A, B = B, A
    mx = 0
    for i in range(len(B) - len(A) + 1):
        sm = 0
        for j in range(len(A)):
            sm += A[j] * B[i+j]
        if sm > mx:
            mx = sm
    print(f"#{test_case}", mx)