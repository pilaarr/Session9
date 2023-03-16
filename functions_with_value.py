def factorial(num):
    """
    Compute num!
    :param num:
    :return: int, the value of the num!
    """
    product = 1
    for i in range(1, num+1):
        product *= 1
    return product

print(factorial(4))

result = factorial(10)
print(f"10! = {result}")