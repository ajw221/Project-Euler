from math import sqrt
def problem1():
    sum = 0
    for i in range(1000):
        if(i%3==0 or i%5==0):
            sum+=i
    return sum

def problem2():
    sum = 0
    i = 0
    while True:
        x = int(round((1/sqrt(5))*(((1+sqrt(5))/2)**i)-(((1-sqrt(5))/2)**i)))
        if(x%2==0):
            sum+=x
        elif x>4000000:
            break
        i+=1
    return sum

def isPrime(num):
    if num<=1:
        return False
    if num<=3:
        return True
    count = 0
    for i in range(1,num+1):
        if num%i==0 or num/i==num or num/i==1:
            count+=1
    if count==2:
        return True
    return 
    
def problem3():
    num = 600851475143
    primes = []
    for i in range(1,round(sqrt(600851475143)),2):
        if(num%i==0 and isPrime(i)):
            primes.append(i)
    return max(primes)

def isPal(result):
    string1 = ''
    string2 = ''
    if len(result)%2==0:
        for i in range(int(len(result)/2)):
            string1+=result[i]
        for i in range(int(len(result)/2),len(result)):
            string2=result[i]+string2
        if string1==string2:
            return True
        else:  
            return False
    else:
        half = int(len(result)/2)
        result = result[0 : half : ] + result[half + 1 : :]
        for i in range(int(len(result)/2)):
            string1+=result[i]
        for i in range(int(len(result)/2),len(result)):
            string2=result[i]+string2
        if string1==string2:
            return True
        else:  
            return False

def problem4():
    num1 = 100
    num2 = 100
    palindrome = ''
    arr = []
    for a in range(num1,999):
        for b in range(num2,999):
            palindrome = str(a*b)
            if isPal(palindrome) and palindrome != '99999' and (b>=450 and a>=450):
                arr.append(palindrome)
    arr.sort()
    return arr[len(arr)-1] 

def problem5():
    for a in range(20,1000000000,20):
        count = 0
        if(a%19==0 and a%20==0):
            for b in range(1,21):
                if(a%b==0):
                    count+=1
            if count == 20:
                return a

def problem6():
    sum = 0
    square = 0
    for i in range(1,101):
        sum+=i**2
        square+=i
    square = square**2
    return square-sum

def fasterPrimes(num):
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

# Using faster prime function for time (not mine)
def problem7():
    count = 1 
    for i in range(3,1000000,2):
        if(fasterPrimes(i)):
            count+=1
            if(count==10001):
                return i
    return count

def problem8():
    string = ('73167176531330624919225119674426574742355349194934'
             +'96983520312774506326239578318016984801869478851843'
             +'85861560789112949495459501737958331952853208805511'
             +'12540698747158523863050715693290963295227443043557'
             +'66896648950445244523161731856403098711121722383113'
             +'62229893423380308135336276614282806444486645238749'
             +'30358907296290491560440772390713810515859307960866'
             +'70172427121883998797908792274921901699720888093776'
             +'65727333001053367881220235421809751254540594752243'
             +'52584907711670556013604839586446706324415722155397'
             +'53697817977846174064955149290862569321978468622482'
             +'83972241375657056057490261407972968652414535100474'
             +'82166370484403199890008895243450658541227588666881'
             +'16427171479924442928230863465674813919123162824586'
             +'17866458359124566529476545682848912883142607690042'
             +'24219022671055626321111109370544217506941658960408'
             +'07198403850962455444362981230987879927244284909188'
             +'84580156166097919133875499200524063689912560717606'
             +'05886116467109405077541002256983155200055935729725'
             +'71636269561882670428252483600823257530420752963450')
    start = 0
    end = 13
    _13 = string[start:end]
    before = 0
    after = 1
    while end!=len(string):
        for a in _13:
            after *= int(a)
        if(before<after):
            before=after
            after = 1
        else:
            after = 1
        start+=1
        end+=1
        _13 = string[start:end]
    return before

def problem9():
    arr = []
    for a in range(0,500):
        for b in range(0,500):
            for c in range(0,500):
                if(a+b+c==1000 and ((a**2)+(b**2)==c**2)):
                    arr.append(a)
                    arr.append(b)
                    arr.append(c)
                    return a*b*c