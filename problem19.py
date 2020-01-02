import datetime
def problem19():
    month = 1
    day = 1
    year = 1901
    count = 0
    while year!=2001:
        date = datetime.datetime(year,month,day).weekday()
        if(date==6 and day==1):
            count+=1
        day+=1
        if(month==1 and day==31):       # January End Test
            month=2
            day=1
        if(year%4==0):                  # February Leap End Test
            if(month==2 and day==29):   
                month=3
                day=1
        if(year%4!=0):                  # February Non-Leap End Test
            if(month==2 and day==28):
                month=3
                day=1
        if(month==3 and day==31):       # March End Test
            month=4
            day=1
        if(month==4 and day==30):       # April End Test
            month=5
            day=1
        if(month==5 and day==31):       # May End Test
            month=6
            day=1
        if(month==6 and day==30):       # June End Test
            month=7
            day=1
        if(month==7 and day==31):       # July End Test
            month=8
            day=1
        if(month==8 and day==31):       # August End Test
            month=9
            day=1
        if(month==9 and day==30):       # September End Test
            month=10
            day=1
        if(month==10 and day==31):      # October End Test
            month=11
            day=1
        if(month==11 and day==30):      # November End Test
            month=12
            day=1
        if(month==12 and day==31):      # Year End Test
            month=1
            day=1
            year+=1
    return count