def isAmicable(num):
    sum = 0
    temp = 0
    for i in range(1,num):
        if(num%i==0):
            sum+=i
    for i in range(1,sum):
        if(sum%i==0):
            temp+=i
    if(temp==num and sum!=num): #IMPORTANT: checking 2nd num is not 1st num#
        return True
    return False

def problem21():
    sum = 0
    for i in range(1,10000):
        if isAmicable(i):
            sum+=i
    return sum