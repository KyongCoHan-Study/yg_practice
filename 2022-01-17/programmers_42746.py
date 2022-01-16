def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x: (x*4)[:4], reverse = True)
    answer = ''.join(numbers)
    # 0인경우 고려 위해 ->int->str 형변환
    return str(int(answer))

