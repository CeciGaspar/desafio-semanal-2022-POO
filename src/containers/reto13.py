def recursive_factorial(num: int):
    if num == 1 or num == 0:
        return 1
    else:
        return num * recursive_factorial(num - 1)

print(recursive_factorial(7))
print(recursive_factorial(10))