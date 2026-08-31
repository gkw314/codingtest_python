def solution(numbers, direction):
    answer = []

        
    if direction == "right":
        # 오른쪽 회전
        answer = [numbers[-1]] + numbers[:-1]
            
    if direction == "left":
        # 왼쪽 회전
        answer = numbers[1:] + [numbers[0]]
            
    return answer