def solution(my_string):
    answer = ''
    gather = "aeiou"
    
    for char in my_string:
        if char in gather:
            continue
        else:
            answer += char
    return answer