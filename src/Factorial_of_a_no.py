#Factorial of a number
def factorial(n):
    fact=1
    for a in range(1,n+1):
        fact*=a;
    return fact
num=int(input("Enter a number"))
print("Factorial of",num,":",factorial(num))
