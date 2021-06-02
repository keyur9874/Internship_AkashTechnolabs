# Square Fun
def square(n):
    return n*n

n = int(input("Enter Number : "))
if n <= 10 :
    print('This number is less than 10')
    print('Square of this Number : ', square(n))
else :
    print('This number is grater than 10')