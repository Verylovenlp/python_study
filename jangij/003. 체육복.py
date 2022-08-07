# 체육복 - 20220807

def solution(n, lost, reserve):
    lost_new = []
    count = 0

    # 본인 꺼 있는지 확인
    for i in lost:
        if i in reserve:
            reserve.remove(i)
            count += 1
        else :
            lost_new.append(i)
    
    # 다른사람 빌려주기
    for i in lost_new:
        for j in reserve:
            if(abs(i-j) <= 1):
                count += 1
                reserve.remove(j)
                break

    answer = n - (len(lost) -  count)
    return answer