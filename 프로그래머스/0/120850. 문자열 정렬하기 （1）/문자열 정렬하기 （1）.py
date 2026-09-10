def solution(my_string):
    answer = []
    number = "01234,,6789"
    for num in my_string:
        if num in number:
            answer.append(int(num))
            
    answer.sort()
    
    return answer