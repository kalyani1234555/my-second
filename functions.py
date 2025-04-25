# def multiply():
#     result = 10.5 * 4
#     return result
#
#
# answer = multiply()
# print(answer)

def multiply(x: float, y: float) -> float:
    """
    Get a multiplier from standard input(stdin)
    :param x: passing the argument to the value x
    :param y: passing the argument to the value y
    :return: will return the multiplication of x ang y value
    """
    result = x * y
    return result


help(multiply)
print("*" * 80)

answer = multiply(10.5, 4)
print(answer)

forty_two = multiply(6, 7)
print(forty_two)

print()
for val in range(1, 5):
    two_times = multiply(2, val)
    print(two_times)
