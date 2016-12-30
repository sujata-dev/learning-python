#To Make a Calculator
def calc(a,b,n):
    if n=='+':
        print("Adding")
        c=a+b
    elif n=='-':
        print("Subtracting")
        c=a-b
    elif n=='*':
        print("Multiplying")
        c=a*b
    elif n=='/':
        print("Dividing")
        c=a/b
    elif n=='%':
        print("Modulus")
        c=a%b
    else:
        print("This operator doesn't exist")
        import sys
        sys.exit()
    return c
a=int(input("Enter 1st number"))
b=int(input("Enter 2nd number"))
n=input("Enter operator")
print("Answer:",calc(a,b,n))
