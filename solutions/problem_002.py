from functools import reduce

def gimme_gimme(array):
    return reduce((lambda x, y: x * y), array)

def solution(array):
    product = gimme_gimme(array)
    return list(map((lambda x: int(product/x)), array))

def solution_without_division(array):
    ans = []
    for index in range(len(array)):
        ans.append(gimme_gimme(array[:index] + array[index+1:]))
    return ans

print(solution([1,2,3,4,5]))
print(solution_without_division([1,2,3,4,5]))
