'''DECORATORS'''
def calc_square(numbers):
    result = []
    for number in numbers:
        result.append(number*number)
    return result

out_square = calc_square(array)
