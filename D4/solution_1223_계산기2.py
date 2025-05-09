T = 10
pri = {'+': 1, '*': 2}
for test_case in range(1, T+1):
    N = int(input())
    st = input()
    equ = ''
    stk = []
    # 중위 표기식 -> 후위 표기식
    for ch in st:
        if ch.isdigit() : # 숫자일 경우
            equ += ch
        else: # 연산자일 경우
            if not stk:
                stk.append(ch)
            else: # 스택이 안 비어있을 경우
                if pri[ch] > pri[stk[-1]]: # 우선 순위 비교
                    stk.append(ch)
                else:
                    while stk and pri[ch] <= pri[stk[-1]]:
                        equ += stk.pop()
                    stk.append(ch)
    while stk:
        equ += stk.pop()
    # 후위 표기식 연산
    for ch in equ:
        if ch.isdigit():
            stk.append(int(ch))
        else:
            op2 = stk.pop()
            op1 = stk.pop()
            if ch == '*':
                stk.append(op2*op1)
            if ch == '+':
                stk.append(op1+op2)
    print(f'#{test_case}', stk.pop())