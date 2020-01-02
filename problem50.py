# 1 hour+ runtime but answer is correct

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

def problem50():                      
    arr = [2]                         
    sums = []
    tracker = []
    for i in range(3,1000000,2):          
        if isPrime(i):                
            arr.append(i)             
    arr.sort() 
    
    for a in arr:
        num = 0
        b = 0
        track = []
        #### DOUBLE DIGITS LOOP ###
        if len(str(a)) <= 2:
            while arr[b] < a and num != a:
                num+=arr[b]
                track.append(arr[b])
                b+=1
            if num == a:
                tracker.append(track)
                sums.append(a)
            else:
                print("{} is not a consecutive prime".format(a))
        ### DOUBLE DIGITS LOOP ###
        ### OTHER LENGTHS LOOP ###
        else:
            count = 0
            while num != a:
                num+=arr[b]
                track.append(arr[b])
                b+=1
                if num>a:
                    count+=1
                    b = count
                    num = 0
                    track = []
            if num==a:
                tracker.append(track)
                sums.append(a)
        ### OTHER LENGTHS LOOP ###
    solve = tracker.index(max(tracker, key=len))
    return sums[solve]