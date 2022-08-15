# 신규 아이디 추천 - 20220815

import re

def solution(new_id):
    
    answer = ''
    # 1단계 : 소문자 치환
    answer = new_id.lower()
    # 2단계 : 제외문자 제거
    answer = re.sub('[^a-z0-9-_\.]', '', answer)
    # 3단계 : 마침표 2번 이상 치환
    answer = re.sub('\.{2}\.*', '.', answer)
    print('3단계 >>> ', answer)
    # 4단계 : 양 끝 마침표 제거
    answer = re.sub('^\.|\.$', '', answer)
    # 5단계 : 빈 문자열이면 a 대입
    if answer == '':
        answer = 'a'
    # 6단계 : 길이가 16자 이상이면 1~15자만 남기기 & 맨 끝 마침표 제거
    answer = re.sub('\.$', '', answer[0:15])
    # 7단계 : 길이가 3이 될 때까지 반복해서 끝에 붙이기
    while len(answer) < 3:
        answer += answer[-1:]
    return answer