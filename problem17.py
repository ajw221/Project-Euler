def problem17():
    # bases = 106 characters
    bases = (
        "",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
        "ten",
        "eleven",
        "twelve",
        "thirteen",
        "fourteen",
        "fifteen",
        "sixteen",
        "seventeen",
        "eighteen",
        "nineteen",
    )
    # ten = 758 characters
    ten = (
        "",
        "",         #3
        "twenty",   #6
        "thirty",   #6
        "forty",    #6
        "fifty",    #5
        "sixty",    #5
        "seventy",  #7
        "eighty",   #6
        "ninety",   #6
    )
    hundred = (
        "",
        "onehundred",
        "twohundred",
        "threehundred",
        "fourhundred",
        "fivehundred",
        "sixhundred",
        "sevenhundred",
        "eighthundred",
        "ninehundred"
    )
    # 1-99     = 864
    # 100-199  = 2157
    # 200-299  = 2157
    # 300-399  = 2357
    # 400-499  = 2257
    # 500-599  = 2257
    # 600-699  = 2157
    # 700-799  = 2357
    # 800-899  = 2357
    # 900-1000 = 2268
    result = ''
    for i in range(1,1000):
        if(i<20 and i>0):
            result += bases[i]
        elif(i>=20 and i<100):
            tens = int(i/10)
            ones = i % 10
            result += (ten[tens] + bases[ones])
        elif(i<1000):
            hundreds = int(i/100)
            tens = int((i % 100)/10)
            ones = i % 10
            if(i%100==0):
                result += hundred[hundreds]
            elif(i%100!=0 and i%100<20):
                result += (hundred[hundreds] + 'and' + bases[i%100])
            else:
                result += (hundred[hundreds] + 'and' + ten[tens] + bases[i%10])
    result+='onethousand'
    return len(result)