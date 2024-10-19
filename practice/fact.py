fact = 1
n = int(input("Enter  a number : "))
for i in range(2,n+1):
	fact *= i
print(str(n)+"! is "+str(fact))
