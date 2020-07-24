#045

"""
total=0
while total<= 50:
    n=int(input('Enter a number: '))
    total += n
    print("The total is  ",total)
"""

#046

"""
n=int(input('Enter a number: '))
while n<5:
    n=int(input('Enter a number: '))
print('The last number you entered was a ',n)
"""

#047

"""
n=int(input('Enter a number: '))
m=int(input('Enter another number: '))
s=n+m
while True:
    ans=input("Do you want to add another number ? ")
    if ans=='y':
        x=int(input('Enter another number: '))
        s += x
    else:
        break
print("The total is ", s)
"""

#048

"""
count=0
name=input('Enter the name of someone you want to invite to the party: ')
print(name, "has now been invited")
while True:
    count +=1
    ans=input('Do you want to invite somebody else? (yes/no)')
    if ans == 'yes':
        name=input('Enter the name of someone you want to invite to the party: ')
        print(name, "has now been invited")
    elif ans == 'no':
        break
    else:
        print('Your answer is not valid :)!')
        break
print('You have invited ',count,' poeple to the party.')
"""

#049

"""
compnum=50
count=0
n=1
while n != compnum:
    n=int(input('Enter a number: '))
    count +=1
    if n < 50:
        print("Your guess is too low.")
    elif n> 50:
        print("Your guess is too high.")
print("Well done, you took ",count," attempts.")
"""

#050

"""
n=int(input('Enter a number between 10 and 20: '))
while not(10 <= n <= 20):
    if n < 10:
        print("Too low")
        print("Try again!")
        n=int(input('Enter a number between 10 and 20: '))
    elif n > 20:
        print("Too high")
        print("Try again!")
        n=int(input('Enter a number between 10 and 20: '))
    
if n == 20 or n==10:
    print("The question does not cover this part! :)")
else:
    print("Thank you")
"""

#051

"""
num=int(input("Enter a number to start 10 green bottle song : "))
print("There are ",num," green bottles hanging on the wall, "\
      ,num," green bottles hanging on the wall"\
      ,"and if 1 green bottle should accidently fall")
num -= 1
while True:
    ans=int(input('How many green bottles will be hanging on the wall?? '))
    
    if ans == num:
        if num ==0:
            print("There are no more bottles hanging on the wall")
            break
        else:
            print("There will be ",num," green bottles on the wall")
            print("There are ",num," green bottles hanging on the wall, "\
              ,num," green bottles hanging on the wall"\
              ,"and if 1 green bottle should accidently fall")
            num -= 1
    
    elif ans != num:
        print("No,try again")
"""
