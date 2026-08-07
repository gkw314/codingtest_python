def solution(price):
    answer = 0
    # 10만원 이상이면 5퍼
    # 30만원 이상이면 10퍼
    # 50만원 이상이면 20퍼 할일
    if price >= 500000:
        answer = price * 0.8
    elif price >= 300000:
        answer =  price * 0.9
    elif price >= 100000:
        answer = price * 0.95
    # price가 해당되지 않으면 그냥 값 출력
    else:
        answer = price
    # price가 주어지면 지불해야할 금액을 리턴
    return int(answer)