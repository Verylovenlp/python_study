"""
- 기능 개발 -
https://school.programmers.co.kr/learn/courses/30/lessons/42586

1. 문제정의
- 현재까지의 진행률(1), 진행 속도(2)가 다른 작업들의 일별 완료 갯수 파악
- 스택 문제

2. 핵심 변수
progresses: 진행률 (list) -> e.g, [93, 92] -> 첫 번째 작업은 93% 완료, 두 번째 작업은 92% 완료됐다는 것
speeds: 작업별 진행 속도 (list) -> e.g, [20, 10] -> 첫 번째 작업은 하루에 20%씩 진척된다는 것

3. 필요 조건
- 일이 조금이라도 남아 있다면, 다음날 배포 (=upper() 조건으로 볼 수 있다)

4. 채점 결과
정확성: 100.0
합계: 100.0 / 100.0
"""
def solution(progresses, speeds):

    # 01. 진행된 퍼센트 -> 남은 퍼센트
    # e.g., [93, 30, 55] -> [7, 70, 45]
    progresses = [100-percent for percent in progresses]

    # 02. 남은 퍼센트 -> 남은 일수로 변경
    # need_day = [7, 3, 9]
    need_day = [ int(remain_percent/speed_day) + 1 if not remain_percent%speed_day == 0 else int(remain_percent/speed_day) for remain_percent, speed_day in zip(progresses, speeds)]

    # 03. 일 별 작업 갯수 계산
    complete = 0
    final_result = list()
    pvt = need_day[0]
    for idx, day in enumerate(need_day):
        if pvt >= day:  complete += 1
        else:
            final_result.append(complete)
            complete = 1
            pvt = day
    final_result.append(complete)
    return final_result
