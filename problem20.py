from math import factorial
def problem20():
    num = str(factorial(100))
    sum = 0
    for i in num:
        sum+=int(i)
    return sum