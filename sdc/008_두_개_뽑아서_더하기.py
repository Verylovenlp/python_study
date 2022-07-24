"""
- 두 개 뽑아서 더하기 -
https://school.programmers.co.kr/learn/courses/30/lessons/68644

1. 문제정의
- 주어진 배열의 두 숫자를 더해 만들 수 있는 숫자의 리스트
- '조합' 문제로 생각됐고, itertools 라이브러리가 생각났다
    - 시험에따라 itertools 사용이 제한적일 수 있으므로 다른 방법도 고민 필요

2. 핵심 변수
numbers: 숫자가 들어있는 리스트 (list)

3. 필요 조건

"""

from itertools import combinations as cb

def solution(numbers):
    return list(sorted(list(set([a+b for (a,b) in list(cb(numbers,2))]))))

numbers = [2,1,3,4,1]
numbers = [5,0,2,7]

numbers = [5,0,2,7]

print(solution(numbers))