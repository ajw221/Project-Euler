def problem29():
    arr = []
    for a in range(2,101):
        for b in range(2,101):
            if not int(pow(a,b)) in arr:
                arr.append(int(pow(a,b)))
    return len(arr)