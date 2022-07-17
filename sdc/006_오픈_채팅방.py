"""
- 오픈 채팅방 -
https://school.programmers.co.kr/learn/courses/30/lessons/42888

1. 문제정의
- 유저 닉네임 변화에 변동에 따른 로그 출력

2. 핵심 변수
record: 유저 출입 로그 (list)

3. 필요 조건
- 유저 입장: "[닉네임]님이 들어왔습니다."
- 유저 퇴장: "[닉네임]님이 나갔습니다."
- 닉네임을 변경할 때는 기존에 채팅방에 출력되어 있던 메시지의 닉네임도 전부 변경
- 채팅방은 중복 닉네임을 허용 -> 단순히 replace 쓰지 말고 id 고려할 것
- 이름이 바뀌는 경우는 두 가지이다 (방 안에서 닉네임 변경할 때만 Change가 찍힌다)

4. 채점 결과
정확성: 6.3
합계: 6.3 / 100.0

5. 고려사항
- 시간초과를 고려할 때, O(2N)으로 생각했으나 잘못된 로직이 있는지 점검
"""

def changeName(uid_dict, uid, new_name):
    uid_dict[uid] = new_name
    return False

def solution(record):
    uid_dict = dict()
    print_logs = None
    for log in record:
        if len(log.split(" ")) > 2: action, uid, nickname = log.split(" ")
        else:   action, uid = log.split(" ")

        action_msg = {
            "Enter": f"{uid}님이 들어왔습니다.",
            "Leave": f"{uid}님이 나갔습니다.",
            "Change": changeName(uid_dict, uid, nickname)
        }

        if not uid in uid_dict: uid_dict[uid] = nickname
        else: changeName(uid_dict, uid, nickname)

        if action_msg[action]:            
            print_logs = f"{print_logs}\t{action_msg[action]}" if print_logs is not None else f"{action_msg[action]}"

    # 02. 최종 이름 변경
    for (uid, nickname) in uid_dict.items():        
        print_logs = print_logs.replace(uid, nickname)
    return print_logs.split("\t")

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
record = ["Enter uid1234 Muzi", "Leave uid1234","Enter uid1234 Muzi", "Leave uid1234", "Enter uid1234 Prodo","Change uid4567 Ryan"]

print(solution(record))