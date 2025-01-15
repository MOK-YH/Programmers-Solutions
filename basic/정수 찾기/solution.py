def solution(num_list, n):
    answer = 0
    if n in num_list:
        answer = 1
    else:
        answer = 0 
    return answer

# 테스트 코드
num_list = [1, 2, 3, 4, 5]
n = 3
result = solution(num_list, n)
print(result)