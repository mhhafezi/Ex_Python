Year = int(input("Enter the year: "))
Month = int(input("Enter the month(1-12) :" ))
Day = int(input("Enter the day: "))
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
print("Today is ",dayofyear ," day of the year")
