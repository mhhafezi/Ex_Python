#069
"""
countries=('Iran','Korea','Canada','Australia','Russia')
print(countries)
country=input("Enter one of these Countries above:")
if country in countries:
    print(countries.index(country))
else:
    print('Wrong !')
"""

#070
"""
countries=('Iran','Korea','Canada','Australia','Russia')
print(countries)
country=input("Enter one of these Countries above:")
if country in countries:
    print(countries.index(country))
else:
    print('Wrong !')
cnumber=int(input("Enter 0,1,2,3 or 4 to see the Country name:"))
print(countries[cnumber])
"""

#071
"""
sports=['basketball','tennis']
sport=input("Enter your favorite sport:")
sports.append(sport)
sports.sort()
print(sports)
"""

#072
"""
subjects=['math','algebra','geometry','biology','chemistry','physics']
print('subjects:',subjects)
s=input("Which one of these subjects you don't like? ")
subjects.remove(s)
print('Updated subjects:',subjects)
"""

#073
"""
foods={1:'',2:'',3:'',4:''}
print('Enter four of your favorite foods: ')
for i in range(1,5):
    print(i,":")
    f=input()
    foods[i]=f
print(foods)
r=int(input("Which one of these foods you want to get rid of?(1-2-3-4)"))
foods.pop(r)
foods=sorted(foods)
"""

#074

"""
colors=['green','red','blue','black','white','gray','orange','purple','yellow','pink']
print(colors)
s=int(input('Enter a number between 0 and 4:'))
e=int(input('Enter a  number between 5 and 9:'))
print('color slice [',s,':',e,'] =  ',colors[s:e])
"""

#075

"""
num4dig= [123,456,789,888]
print('List of three-digit numbers:')
for i in num4dig:
    print(i)
number=int(input('Enter a three-digit number:'))
if number in num4dig:
    print(num4dig.index(number))
else:
    print('That is not in the list')
"""

#076
"""
names=[]
print('Enter the name of 3 people you want to invite to the party:')
for i in range (1,4):
    print(i,":")
    n=input()
    names.append(n)
while True:
    conti=input('Do you want to add another: ')
    if conti=='no':
        print('You have invited ',len(names),'people to the party.')
        break
    elif conti=='yes':
        n=input('Enter the name:')
        names.append(n)
"""

#077

"""
names=[]
print('Enter the name of 3 people you want to invite to the party:')
for i in range (1,4):
    print(i,":")
    n=input()
    names.append(n)
while True:
    conti=input('Do you want to add another: ')
    if conti=='no':
        print('You have invited ',len(names),'people to the party.')
        break
    elif conti=='yes':
        n=input('Enter the name:')
        names.append(n)
print(names)
name=input('Enter one of the names in the list:')
print('Position of',name,'in the list :  ',names.index(name))
print('Do you still want ',name,'to come to the party? ')
ans=input()
if ans == 'no':
    names.remove(name)
    print(names)
if ans=='yes':
    print('The question does not involve this part!  :)  ')
"""

#078

"""
tvprogs=['SpongeBob SquarePants','The Joy of Painting','The Umbrella Academy','Killing Eve']
for i in tvprogs:
    print(i)

show=input("Enter another show:")
posi=int(input("Enter the position of the show you want it to be (1-2-3-4): "))
tvprogs.insert(posi-1,show)
print('New Position of tv programms: ')
for i in tvprogs:
    print(i)
"""

#079

"""
nums=[]
for i in range(1,4) :
    num=int(input('Enter a number : '))
    nums.append(num)
    print('nums = ',nums)
ans=input('Do you still want the last number ? ')
if ans== 'no':
    nums.remove(num)
    print('nums = ',nums)
else:
    print('The question does not involve this part!  :)  ')
"""
