import re
def solution(new_id):
    # 1단계
    answer = new_id.lower()
    # 2단계
    answer = re.sub('[^a-z0-9\-\_\.]', '', answer) 
    # 3단계
    answer = re.sub('\.{2,}', '.', answer) 
    # 4단계
    answer = re.sub('^\.|\.$', '', answer) 
    # 5단계
    answer = 'a' if answer == '' else answer 
    # 6단계
    answer = answer[:15] if len(answer) > 15 else answer 
    answer = re.sub('\.$', '', answer) 

    #7단계
    while True: 
        if len(answer) > 2: 
            break 
        answer = answer + answer [-1]

    return answer

new_id = "...!@BaT#*..y.abcdefghijklm"
print(solution(new_id))