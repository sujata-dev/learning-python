#Removing duplicate items from a list
def duplicate(a):
    x=[]
    for y in a:
        if y not in x:
            x.append(y)
    print(x)
a1=input("Enter string")
duplicate(a1)
