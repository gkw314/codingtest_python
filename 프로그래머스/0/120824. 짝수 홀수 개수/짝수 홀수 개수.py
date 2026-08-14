def solution(num_list):
    answer = []
    even_count = 0
    odd_count = 0
    
    for i in num_list:
        if i % 2 == 0:
            even_count += 1
        else : 
            odd_count += 1
            
    answer = [even_count, odd_count]
            
    return answer