def solution(money):
    answer = []
    # 아메리카노 : 5500
    # 가진돈: money
    # 결과1: 최대로 마실 수 있는 아메리카노 수
    # 1. money / 5500
    # 결과2: 최대로 마시고 남은 잔돈
    # 2. money - (1결과*5500) 
    max_cof = money // 5500
    change = money % 5500

    
    return [max_cof, change]