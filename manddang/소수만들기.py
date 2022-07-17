from collections import deque
tmp = []

def do_something(comb):
    return list(comb)
    
    
def dfs(comb: deque, depth: int):
    M = 3
    if len(comb) == M:  # 종료 조건 1 : M개를 모두 선택했을 때
        tmp.append(do_something(comb))  # 선택 후의 알고리즘 호출
        return
    elif depth == len(some_list):  # 종료 조건 2: 리스트의 마지막 까지 탐색했을 때
        return
    # 현재 depth의 값 포함 재귀 호출
    comb.append(some_list[depth])
    dfs(comb, depth + 1)
    # 현재 depth의 값 미포함 재귀 호출
    comb.pop()
    dfs(comb, depth + 1)
    
def solution(nums):
    answer = 0
    cnt = 0
    global some_list 
    some_list = nums


    # 3개 숫자를 선택하기 (그리디)
    dfs(deque(), 0)
    
    # 소수 인지 확인하기
    for i in tmp:
        sum_value = sum(i)
        check_prime = 0
        
        for j in range(1, sum_value + 1):
            if (sum_value % j) == 0:
                check_prime += 1
        if check_prime == 2:
            cnt += 1
    answer = cnt

    
    
    return answer
