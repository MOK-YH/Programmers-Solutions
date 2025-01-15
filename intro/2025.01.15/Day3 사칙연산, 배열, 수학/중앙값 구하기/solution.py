def solution(array):
    answer = 0
    array.sort()
    return array[len(array) // 2]

array = [1, 2, 7, 10, 11]
result = solution(array)
print(result)

array2 = [9, -1, 0]
result2 = solution(array2)
print(result2)