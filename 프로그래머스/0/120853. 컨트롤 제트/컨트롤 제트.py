def solution(s):
    arr = s.split()
    s_sum = 0
    for i in range(len(arr)):
        if arr[i] == 'Z':
            s_sum -= int(arr[i - 1])
        else:
            s_sum += int(arr[i])
            
    return s_sum