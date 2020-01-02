# Using faster prime function for time (not mine)
def isPrime(num):
    if num <= 3:
        return True
    if num <= 1 or num%2==0 or num%3==0:
        return False
    i = 5
    while(i*i <= num): 
        if (num%i==0 or num%(i + 2)==0): 
            return False
        i+=6
    return True

def problem10():
    sum = 2
    for a in range(3,2000000,2):
         if isPrime(a):
            sum+=a
    return sum