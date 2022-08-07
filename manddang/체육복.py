def check_back(cloth,i,n):
    
    # 앞학생이 여분을 가져왔고 뒷 학생이 잃어버렸으면, 전달
    if (i < n) and cloth[i+1] == 0:
        cloth[i+1] = 1
        #print(i, cloth)
    elif (i == n) and cloth[i-1] == 0:
        cloth[i-1] = 1
        #print(i, cloth)
    # 앞학생이 여분을 가져왔고 뒷 학생도 있고, 
    if (i < n) and (cloth[i+1] == 1) and (cloth[i-1] == 0):
        cloth[i-1] = 1        
        #print(i, cloth)
        
    # 마지막 햑생은 여유분이 있고 앞에 학생이 없으면, 전달

    return cloth


def solution(n, lost, reserve):
    # n은 전체 학생수
    # lost는 체육복을 도난당한 학생들의 번호가 담긴 배열
    # reserve는 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열
    answer = 0
    lost = set(lost)
    reserve = set(reserve)
    
    #학생들 일렬화
    cloth = [1 for i in range(n+1)]
    cloth[0] = 3
    
    # 도난 당한 학생 표시
    for i in lost:
        cloth[i] = 0
    #print(cloth)
    
    # 도난 당한 사람이 여벌의 체육복이 있으면 가져온것으로 표기
    save = lost.intersection(reserve)
    for i in save:
        cloth[i] = 1   
        
        
    # 여벌의 체육복 앞뒤 확인
    for i in reserve:       
        cloth = check_back(cloth,i,n)        
        
        answer = cloth.count(1)
        
                
    
    
    return answer
