def solution(numbers):
    result = []
    for i in numbers:
        result.append(i*2)
    return result


numbers = [1, 2, 3, 4, 5]
result = solution(numbers)
print(result)