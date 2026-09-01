def solution(box, n):
    answer = 1
    
    
    for i in box:
        # 주사위 몇개 들어가는지 구하기
        count = i // n
        # 지금까지 계산한 개수에 현재 방향의 개수를 곱하기
        answer = answer * count
            
    return answer