"""
- 문자열 압축 -
https://school.programmers.co.kr/learn/courses/30/lessons/43165

1. 문제정의
- 가장 짧은 문장을 만들 수 있도록, 최적의 압축 길이 탐색
- n-gram

2. 핵심 변수
S: 연속적인 알파벳 (str)

3. 필요 조건
- x

4. 채점 결과
정확성: 100.0
합계: 100.0 / 100.0
"""

def n_gram(S, n):
    prv_window = ""
    encoded_S = ""
    cout = 1
    start_idx = 0
    while True:
        if start_idx + n > len(S):  
            remainder = S[start_idx:]
            encoded_S = encoded_S + str(cout) + remainder if cout > 1 else encoded_S + remainder
            break 

        cur_window = S[start_idx:start_idx+n]
        if prv_window == cur_window:    cout +=1
        else:
            encoded_S = encoded_S + str(cout) + cur_window if cout > 1 else encoded_S + cur_window
            prv_window = cur_window
            cout = 1
        start_idx += n
    return encoded_S

def solution(S:str) -> int:    
    best_encoded_len = len(S)
    for window_size in range(len(S)-1, 0, -1):
        encoded_txt = n_gram(S, window_size)
        if best_encoded_len > len(encoded_txt): best_encoded_len = len(encoded_txt)
    return best_encoded_len
