def Fibonacci(n): 
    if n<=0: 
        print("This number is not valid for fibonacci") 
    elif n==1: 
        return 0
    elif n==2: 
        return 1
    else: 
        return Fibonacci(n-1)+Fibonacci(n-2)

"""
def Fibonacci_list(n):
    L=[0,1]
    for i in range(n-2):
        L.append(L[-1]+L[-2])
    return L
"""

def Fibonacci_list(n):
    L=[0,1]
    for i in range(3,n+1):
        L.append(Fibonacci(i))
    return L
