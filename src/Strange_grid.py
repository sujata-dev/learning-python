#Strange Grid
r,c=input().strip().split(' '); r=int(r); c=int(c)
if r%2!=0:	val=(((r//2)*10)+((c-1)*2))
else:	val=((((r-1)//2)*10)+1+((c-1)*2))
print(int(val))
