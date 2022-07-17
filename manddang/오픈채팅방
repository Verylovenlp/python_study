## 관련 문제: https://school.programmers.co.kr/learn/courses/30/lessons/42888



global dic 
dic = {}


def nick_name_update(ID,nick_name):
    ## 닉네임 저장
    
    dic[ID] = nick_name
    
    return 


def solution(record):
    answer = []
    tmp_answer = []
    
    
    ## 닉네임 업데이트 by dict
    for i in record:
        action = i.split(sep=' ')
        if action[0] == 'Enter':
            nick_name_update(action[1],action[2])
            tmp_answer.append([action[0],action[1]])
            
        elif action[0] == 'Leave':
            tmp_answer.append([action[0],action[1]])
            
        elif action[0] == 'Change':
            nick_name_update(action[1],action[2])

    
    
    #안내 메세지 송출
    for j in tmp_answer:
        if j[0] == 'Enter':
            answer.append(str(dic[j[1]]) + '님이 들어왔습니다.')
        if j[0] == 'Leave':
            answer.append(str(dic[j[1]]) + '님이 나갔습니다.')   
    
    return answer
