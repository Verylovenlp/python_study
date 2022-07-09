"""
- 타겟 넘버 -
https://school.programmers.co.kr/learn/courses/30/lessons/43165

1. 문제정의
- 입력된 숫자들을 더하고 빼서 목표 숫자 달성 경우의 수
- 재귀함수

2. 핵심 변수
numbers: 음이 아닌 정수 (list)
target: 정수들을 조합해 만들어야 하는 값 (int)

3. 필요 조건
- n개의 음이 아닌 정수
- 입력된 순서 그대로 연산

4. 채점 결과
정확성: 100.0
합계: 100.0 / 100.0
"""

def search(numbers:list, target:int, start_idx:int, sum:int=0) -> int:    
    if len(numbers) == start_idx:
        if sum == target: return 1
        else:             return 0
    else:
        return search(numbers, target, start_idx+1, sum+numbers[start_idx]) + search(numbers, target, start_idx+1, sum-numbers[start_idx])
    
def solution(numbers:list, target:int) -> int:    
    return search(numbers, target, 0, 0)
