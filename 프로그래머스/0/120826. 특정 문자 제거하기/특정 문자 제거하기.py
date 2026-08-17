def solution(my_string, letter):
    answer = ''
    for i in my_string:
        # i안에 letter이 있는지??
        if i != letter:
            # i가 letter이 아니면 answer에 넣기
            answer += i
            
    return answer