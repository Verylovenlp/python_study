
"""
- 가장 큰 수 -
https://school.programmers.co.kr/learn/courses/30/lessons/42746

1. 문제정의
- 주어진 배열 숫자를 이어 붙여 가장 큰 수 만들기
- 몇 가지 방법론이 있을 듯

2. 핵심 변수
numbers: 숫자가 들어있는 리스트 (list)

3. 필요 조건
- [0, 0, 0] 입력 대한 고려 ('000'이 아니라 '0'이 정답)

"""

# (1) 모든 경우의 수를 고려하니까 상당수 케이스 시간초과
# from itertools import permutations as pm
# def solution(numbers):
#     return str(max([int(("").join(num)) for num in pm(list(map(str, numbers)))]))

# (2) 이 코드만으로도 어느정도 해결이 되지만, [9,5,3,34,30] 처럼 두 번째 자리 숫자를 고려해야 3보다 34가 앞으로 간다
# numbers = list(sorted(numbers, key=lambda x:(int(str(x)[0]), -len(str(x)), x), reverse=True))

def _len(num):  return len(str(num))
def _equalizeMaxLen(max_len, num):
    (full, remain) = divmod(max_len, _len(num))
    new_num = str(num) * full + str(num)[:remain] 
    return new_num

def solution(numbers):
    # 모든 값이 0인 케이스 고려
    if sum(numbers) == 0:   return '0'

    # 자릿수 맞추기 1
    max_len = len(str(max(numbers))) * 4

    # 자릿수 맞추기 2
    numbers = [(num,str(num)) if _len(num) == max_len else (num, _equalizeMaxLen(max_len, num))  for num in numbers]
    numbers = list(sorted(numbers, key=lambda tupl:tupl[1], reverse=True))
    numbers = [str(k) for k, num in numbers]
    return str(int(("").join(numbers)))

    # 1 ~ 6번 케이스가 해결되지 않아 고민한 결과
    # 끝자리 4자리를 늘리는 방식이 잘못됨 -> [30, 3021] 예시 -> 정답 3030,21 / 틀림 3021, 30
# numbers = [3, 35, 34, 32, 5, 9]
# numbers = [6, 10, 2]	
# numbers = [340,3405]
numbers = [3, 30, 31, 34, 33, 5, 9]
# numbers = [1, 11, 111, 1111]
# numbers = [0, 0, 0, 0, 0, 0]
# numbers = [30, 3021]
# "0"
# "1111111111"

# "95343333130"

# "3405340"
# 9 5 35 34 3 32
print(solution(numbers))