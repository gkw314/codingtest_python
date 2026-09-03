def solution(numbers):
    answer = 0

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            num_v = numbers[i] * numbers[j]

            if answer < num_v:
                answer = num_v

    return answer