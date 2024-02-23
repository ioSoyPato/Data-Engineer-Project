def factorial(n,acc=1):
    if n ==0:
        return acc
    else:
        return factorial(n-1,n*acc)
    
print(factorial(5))