def solution(n):
    answer = 0

    for i in range(1, n+1):
        count = 0
        
        for j in range(1, i+1):
            # 나머지가 0이면 j는 i약수
            if i % j == 0:
                count += 1
        # 약수가 3개이상이면
        if count >= 3:
            answer += 1

    return answer