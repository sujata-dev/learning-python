#calculating the absolute difference between the sums of diagonals of a square matrix NXN, 
n=int(input());arr=[]
sum1,sum2=0,0
for i in range(n):
    i=[int(arr) for arr in input().split(' ')]
    arr.append(i)
for i in range(n):
	sum1=sum1+arr[i][i]
	sum2=sum2+arr[i][n-i-1]
print(abs(sum1-sum2))
