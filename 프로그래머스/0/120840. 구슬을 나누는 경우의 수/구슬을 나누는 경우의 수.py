def solution(balls, share):
    balls_fac = 1
    share_fac = 1
    minus_fac = 1

    # balls!
    for i in range(1, balls + 1):
        balls_fac *= i

    # share!
    for i in range(1, share + 1):
        share_fac *= i

    # (balls - share)!
    for i in range(1, balls - share + 1):
        minus_fac *= i

    answer = balls_fac // (share_fac * minus_fac)

    return answer