def Fibonacci(n): 
    if n<=0: 
        print("This number is not valid for fibonacci") 
    elif n==1: 
        return 0
    elif n==2: 
        return 1
    else: 
        return Fibonacci(n-1)+Fibonacci(n-2) 
