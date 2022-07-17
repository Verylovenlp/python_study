"""
- 더 맵게 -
https://school.programmers.co.kr/learn/courses/30/lessons/42626

1. 문제정의
- 주어진 음식 스코빌을 모두 K이상으로 만드는 연산 횟수
- 왜 힙(Heap) 문제지?

2. 핵심 변수
scoville: 음식별 스코빌 지수 (list)
K: 스코빌 지수 임계치 (int)

3. 필요 조건
- 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
- 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우에는 -1을 return

4. 채점 결과
정확성: 76.2
효율성: 23.8
합계: 100.0 / 100.0
"""

    
# def solution(scoville, K):
#     """
#     채점 결과) 정답 O / 시간초과
#     정확성: 76.2
#     효율성: 0.0
#     합계: 76.2 / 100.0

#     왜 느릴까?)
#     1. 반복적인 정렬 -> 실질적으로 0,1 인덱스만 연산 -> Root 값만 가져오기 위해서는 힙이 최고
#     2. 반복적인 필터 사용
#     """
#     cout = 0
#     while len(list(filter(lambda x: x<K, scoville))) > 0:
#         # K이상 스코빌을 만들 수 없는 경우
#         # scoville=[1,2] / K=7 같은 입력
#         if len(scoville) < 2: return -1
#         cout += 1
#         # 01. 스코빌 지수 오름차순 정렬    
#         scoville = list(sorted(scoville))
#         scoville = [scoville[0] + (scoville[1] * 2)]  + scoville[2:]
#     return cout


import heapq as hq
def solution(scoville, K):
    cout = 0
    hq.heapify(scoville)
    cout = 0
    while True:
        # K이상 스코빌을 만들 수 없는 경우
        # scoville=[1,2] / K=7 같은 입력
        if len(scoville) < 2 and scoville[0] < K:
            return -1
        elif scoville[0] < K:
            first = hq.heappop(scoville)
            second = hq.heappop(scoville)
            hq.heappush(scoville, first + second*2)
            cout += 1
        else:
            break
    return cout
