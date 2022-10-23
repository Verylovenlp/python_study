def solution(people, limit):
    people.sort()
    totalCount = 0
    
    while len(people) > 0 :
        targetOne = people[0]

        maxWeight = 0  # 2명 무게 합계
        choiceIdx = 0  # 2명이 가능한 경우 선택된 사람
        for idx, val in enumerate(people) :
            if idx == 0 :
                continue

            #print("out : ", targetOne, val)
            # 구명보트 무게 제한 체크하기
            sumWeight = targetOne + val
            if sumWeight > maxWeight and sumWeight <= limit :
                maxWeight = sumWeight
                choiceIdx = idx

            if sumWeight > limit :
                break;

        if maxWeight > 0 :  # 2명이 가능한 조건일때
            del people[choiceIdx]

        del people[0]       
        totalCount += 1

    return totalCount