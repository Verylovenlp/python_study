## 관련문제: https://school.programmers.co.kr/learn/courses/30/lessons/42576

#### 결과 ####
# 정확성: 50 #
# 효율성: 0  #
##############

# 해시문제로 다시풀것

def solution(participant, completion):
    answer = ''
    for completion_name in completion:
        if  completion_name in participant:
            participant.remove(completion_name)
    answer = participant[0]
    return answer
