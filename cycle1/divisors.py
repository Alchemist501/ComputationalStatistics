num = int(input("Enter the number : "))
ls = []
for i in range(1,num+1):
	if(num % i != 0):
		continue
	ls.append(i)
print(ls)
