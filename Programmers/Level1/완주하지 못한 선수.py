# 런타임 에러
# def solution(participant, completion):
#     setPart = set(participant)
#     setCom = set(completion)
#     return list(setPart.difference(setCom))

import collections

def solution(participant, completion):
    unfinished = collections.Counter(participant) - collections.Counter(completion)
    return list(unfinished.keys())[0]

participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion = ["josipa", "filipa", "marina", "nikola"]


print(solution(participant, completion))