flag = True
start = int(input("Enter the starting number : "))
end = int(input("Enter the ending number : "))
if start < 2:
	start = 2
while start <= end:
	for i in range(2,end + 1):
		if start % i == 0 and start != i:
			flag = False
			break
	if flag:
		print(start)
	start += 1
	flag = True

