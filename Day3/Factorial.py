# Find Factorial of Given Number

def factorial(n):
    if n== 0:
        return 1
    return factorial(n-1) * n

n = int(input("Enter number for Find factorial : "))
print(factorial(n))