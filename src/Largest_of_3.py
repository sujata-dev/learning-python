#Largest of 3 numbers
def largest(a,b,c):
    if a>b and a>c:
        print(a,"is the largest")
    elif b>a and b>c:
        print(b,"is the largest")
    elif c>a and c>a:
        print(c,"is the largest")
    else:
        print(a,",",b,"and",c,"are equal")
a1=input("Enter 1st number")
a2=input("Enter 2nd number")
a3=input("Enter 3rd number")
largest(a1,a2,a3)
