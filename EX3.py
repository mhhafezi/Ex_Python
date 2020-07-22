y = int(input("Enter a Year: "))

# Leap Year Check


if y % 400 == 0:
    print(y, "is a Leap Year")
elif y % 100 == 0:
    print(y, "is not a Leap Year")
elif y % 4 == 0:
    print(y, "is a Leap Year")
else:
    print(y, "is not a Leap Year")
