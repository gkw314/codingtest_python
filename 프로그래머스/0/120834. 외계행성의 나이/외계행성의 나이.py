def solution(age):
    answer = ''
    char = 'abcdefghij'
    
    # 숫자를 문자열로 바꾸기
    for i in str(age):
        answer += char[int(i)]
    return answer