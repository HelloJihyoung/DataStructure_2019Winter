# 런타임 에러
# import calendar
# def solution(a, b):
#     answer = ''
#     day = ['SUN','MON', 'TUE', 'WED', 'THU','FRI','SAT']
#     print(calendar.weekday(2016, a, b))
#     answer = day[(calendar.weekday(2016, a, b))+1]
#     return answer

def solution(a, b):
    day = ["THU","FRI","SAT","SUN","MON","TUE","WED"]
    month = [31, 29, 31, 30, 31, 30 , 31, 31, 30, 31, 30, 31]
    
    return day[(sum(month[:a-1]) + b) % 7]