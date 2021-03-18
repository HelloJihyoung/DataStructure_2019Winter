#import re
def solution(s):
    if len(s) == 4 or len(s) == 6:
        for i in s:
            if not i.isdigit():
                return False
        return True
    return False
    
    # numbers = re.findall("\d+", s)
    # if len(numbers) == len(s) and (len(s) = 4 or len(s) 6):
    #     return True
    # else:
    #     return False

s = "a234"
print(solution(s))