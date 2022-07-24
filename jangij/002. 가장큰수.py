# 숫자 배열 만들기
def solution(numbers):
    answer = []
    
    for num in numbers:
        if len(answer) == 0:
            answer.append(num)
            continue

        flag = True
        for idx, val in enumerate(answer):
            if compare(num, val):
                answer.insert(idx, num)
                flag = False
                break
        if flag:
            answer.append(num)

    return answer

# 숫자크기 비교
def compare(a, b):
    a = str(a)
    b = str(b)
    num = len(a) - len(b)

    if num > 0:
        target = a
        origin = b
    else:
        target = b
        origin = a

    for v in range(0, len(origin)-(len(target)%len(origin))):
        target = target + "0"

    loop = int(len(target)/len(origin))

    flag = False
    o_num = int(origin)
    for v in range(0, loop):
        t_num = int(target[v*len(origin):(v+1)*len(origin)])
        if o_num > t_num:
            flag = True
            break

    if flag:
        return True
    else:
        return False