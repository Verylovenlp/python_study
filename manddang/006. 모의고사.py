#관련문제: https://school.programmers.co.kr/learn/courses/30/lessons/42840


def student_answer(answers):
    student_1,student_2,student_3 = [],[],[]
    #수포자1,2,3 정답지 설정
    tmp =  [1,2,3,4,5]
    for i in range(0,len(answers)):
        student_1.append(tmp[i%5])    
    
    tmp = [2, 1, 2, 3, 2, 4, 2, 5]
    for i in range(0,len(answers)):
        student_2.append(tmp[i%8])
        
    tmp = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for i in range(0,len(answers)):
        student_3.append(tmp[i%10])
        
        
    return student_1, student_2, student_3


def solution(answers):
    answer = []
    student_1,student_2,student_3 = student_answer(answers)
    cnt_1,cnt_2,cnt_3 = 0,0,0
    
    for i in range(0,len(answers)):
        
        if student_1[i] == answers[i]:
            cnt_1 +=1
        if student_2[i] == answers[i]:
            cnt_2 +=1
        if student_3[i] == answers[i]:
            cnt_3 +=1

    # 답 저장
    tmp_answer = max(cnt_1,cnt_2,cnt_3)
    
    if tmp_answer == cnt_1:
        answer.append(1)
    if tmp_answer == cnt_2:
        answer.append(2)
    if tmp_answer == cnt_3:
        answer.append(3)


    return answer
