def solution(emergency):
    answer = []
    # 두수 비교해서 더 큰값 우선순위
    # emergency에서 숫자를 하나씩 꺼낸다.
    for i in emergency:
        # 순위를 1로 시작한다.
        rank = 1
        
        # emergency를 다시 순회하면서 다른 숫자들과 비교한다.
        for j in emergency:
            # 현재 숫자보다 큰 숫자가 있다면
            if j > i:
                # 순위를 1 증가시킨다.
                rank += 1
                
        answer.append(rank)
            
    return answer