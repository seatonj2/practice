#practice file
def sum(n):
    "adds numbers from 1 to, and including, n"
    result = 0
    for i in range(1,n+1):
        result = result + i
    return result

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
x = 10
y = 20
z = x * y

print (x ,"+",y ,"=",z)

print ("Sum of 1 to",x,"=",sum(x))

print ("Factorial has been called with n = 5 \n","=",factorial(5))
