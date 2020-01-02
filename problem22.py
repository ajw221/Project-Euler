import os
def problem22():
    letters = {
        'A':1,
        'B':2,
        'C':3,
        'D':4,
        'E':5,
        'F':6,
        'G':7,
        'H':8,
        'I':9,
        'J':10,
        'K':11,
        'L':12,
        'M':13,
        'N':14,
        'O':15,
        'P':16,
        'Q':17,
        'R':18,
        'S':19,
        'T':20,
        'U':21,
        'V':22,
        'W':23,
        'X':24,
        'Y':25,
        'Z':26,
    }
    file = open("p022_names.txt", "r")
    string = file.read().replace('"', "")
    arr = string.split(",")
    arr.sort()
    sum = 0
    track = 1
    for name in arr:
        word = 0
        for letter in name:
            word += letters[letter]
        sum+=(word*track)
        track+=1
    return sum
print(problem22())