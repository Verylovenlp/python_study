"""
- 완주하지 못한 선수 -
https://school.programmers.co.kr/learn/courses/30/lessons/42576

1. 문제정의
- 마라톤 미완주자명 출력
- 두 배열 비교 문제

2. 핵심 변수
participant: 마라톤 참가자명 (list)
completion: 마라톤 완주자명 (list)

3. 필요 조건
- 마라톤 참가자 수 (1 <= n <= 100,000)
- 출력은 항상 한 명
- 동명 이인 존재 가능
- return -> 완주하지 못한 사람

4. 채점 결과
정확성: 50.0
효율성: 50.0
합계: 100.0 / 100.0
"""
def solution(participant:list, completion:list) -> str:    
    # 1. set()을 이용한 차집합
    # -> 동명이인이 존재하므로 사용 불가
    # incomplete_runner = list(set(participant) - set(completion))[0]

    # 2. collention (프로그래머스에서 허용된 라이브러리)을 이용한 차집합
    from collections import Counter

    """
    Counter(participant): 각 참가자별 빈도수가 저장된 Dictionary 형태
        e.g., Counter({'leo': 2, 'kiki': 1, 'eden': 1})

    Counter(participant) - Counter(completion): 두 Dictionary의 빼기
        e.g., Counter({'leo': 1})

    .elements(): Dictionary의 .keys()와 유사
    """
    incomplete_runner = list((Counter(participant) - Counter(completion)).elements())[0]   
    return incomplete_runner