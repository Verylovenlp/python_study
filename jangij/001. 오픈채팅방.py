# 공통문제 - 20220717

def solution(record):
    answer = []

    # 닉네임 디셔너리
    nick_name = {}
    for item in record:
        item_list = item.split()
        if item_list[0] != "Leave":
            nick_name[item_list[1]] = item_list[2]

    # 관리자 출력메시지
    for item in record:
        item_list = item.split()
        if item_list[0] == "Enter":
            answer.append(nick_name.get(item_list[1]) + "님이 들어왔습니다.")
        elif item_list[0] == "Leave":
            answer.append(nick_name.get(item_list[1]) + "님이 나갔습니다.")

    return answer