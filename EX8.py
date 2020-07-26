def dayofyear(Year,Month,Day):
    if Year % 400 == 0:
        leap = True
    elif Year % 100 ==0:
        leap = False
    elif Year % 4 ==0:
        leap = True
    else :
        leap = False

    months = [31,28,31,30,31,30,31,31,30,30,30,31]
    if leap == True :
        months[1] = 29
    m=0
    for i in range(0,Month-1):
        m += months[i]
        
    dayofyear = m + Day
    return ("Today is ",dayofyear ," day of the year")

print(dayofyear(1996,12,3))
print(dayofyear(2000,3,1))
