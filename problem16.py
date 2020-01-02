from math import pow
def problem16():
    string = '%f' % pow(2,1000)
    string = string.replace(".", "")
    sum = 0
    for i in string:
        sum+=int(i)
    return sum