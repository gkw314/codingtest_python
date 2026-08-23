def solution(rsp):
    answer = ''
    r = "2"
    s = "0"
    p = "5"
    
    for i in rsp:
        if i == r:
            answer += s
        elif i == s:
            answer += p
        else:
            answer += r
    return answer