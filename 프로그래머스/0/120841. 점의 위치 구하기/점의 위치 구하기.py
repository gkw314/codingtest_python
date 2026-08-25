def solution(dot):
    answer = 0
    x = dot[0]
    y = dot[1]
    
    # x,y 양수 1사분
    # y만 양수 2사분
    # x,y 음수 3사분
    # x만 양수 4사분

    if x > 0 and y > 0:
        answer = 1
        return answer
    elif x < 0 and y > 0:
        answer = 2
        return answer
    elif x < 0 and y < 0:
        answer = 3
        return answer
    else:
        answer = 4
        return answer
